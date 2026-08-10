---
layout: post
title: "Knowing When You're Done Talking: What Building a Voice Pipeline Taught Me"
date: 2026-08-10
categories: [AI, Tools]
excerpt: > #
  Building a small dictation tool turned into a tour of every place a speech-to-speech pipeline has to guess when you're done talking -- and where that guessing goes wrong.
math: false
---

Say "turn off the lights" to a voice assistant, pause for half a breath, and it can already be answering — "Which lights?" — before you get to "...in the bedroom." Nothing here is a bug. The speech got transcribed correctly, the language model reasoned correctly, the pipeline did exactly what it was built to do. It just didn't know you weren't finished yet.

That gap — between what a system can *transcribe* and what it actually understands about *when a person is done talking* — turned out to be the whole story once I started building a voice pipeline.

## Why such a pipeline?

A few things I've wanted for a while:

- **Brainstorming with a personal assistant while not sitting at a keyboard** — pacing around thinking out loud is a different mode of thinking than typing, and it only works if the assistant doesn't need hands on a keyboard.
- **Steering a robot** — moving through physical space rules out typing outright; voice is the only input channel that keeps up.
- **Text input while vibe coding** — dictating instead of typing makes it cheap to hand an LLM a lot of context at once, instead of trimming a prompt down to whatever's fast to type.

Two things triggered me to pick this topic up again recently. First, the release of the Parakeet model — genuinely the most precise speech-to-text model I've run on my own machine so far. Second, a HuggingFace blog post showing how individual models — STT, an LLM, TTS — can be stitched into a pipeline that actually feels like a good user experience, not just a chain of demos bolted together.

A voice assistant that actually holds a conversation is really three models stitched together: speech-to-text (STT) turns what you said into words, a language model (LLM) decides what to say back, and text-to-speech (TTS) turns that reply back into audio. Speech in, text, reasoning, text, speech out — that's the pipeline this post is about, and the LLM in the middle is what turns "transcribe this" into "have a conversation."

Stitching those three together looks like an audio engineering problem from the outside — recognize the words, generate a response, say it back. Build one, even a small one, and it turns into something else: a long series of decisions about *when*. When does recording start. When does it end. When is a transcript "done enough" to hand to the LLM. When should the reply start playing. When should it stop, mid-sentence, because the person clearly wants to say something else. When is this conversation actually over.

Every one of these is a small trigger, usually invisible until it's wrong. Get one of them wrong and the whole thing feels either laggy or rude — even if the STT is perfect and the LLM's answer is exactly right. This post walks through building a speech pipeline from the simplest possible version up to a full conversational loop, one added complexity at a time, and each stage turns out to just be a new instance of the same underlying question: how does the system know it's time to act.

## 1. The naive baseline: push a button, speak, push it again

The simplest version of "speech to text" doesn't need any of the machinery below. I built exactly this as a small personal tool: a system-wide dictation daemon. Press a hotkey, it opens the mic. Press it again, it closes the mic, runs the whole recording through an on-device STT model in one shot, and types the result into whatever text field has focus.

This already has two trigger points, they're just both manual: *recording starts* (button press) and *recording ends* (button press). For a single person dictating a paragraph, that's genuinely enough — no ambiguity, no guessing, the human is the trigger. It falls apart the moment you add a second speaker (now you need diarization — figuring out *who* is talking, a completely different axis from *when*, and one this post deliberately leaves aside; I wrote about that problem separately in [Transcription of audio files](https://quantitative-thinking.com/2023/03/Transcription_of_audio_files/)). But for a single-speaker dictation tool it's a solid, boring baseline.

Keep those two triggers in mind — record-start, record-end — because almost everything from here on is either automating one of them, or discovering that there are more of them hiding in the pipeline than you thought.

## 2. The pile-up problem, and VAD as the first automatic trigger

The naive version has an obvious flaw once recordings get long: nothing happens until you press stop. Dictate for 30 seconds, and only *after* that final button press does the model start transcribing — meaning you're staring at a blank text field for however long inference takes, on top of the 30 seconds you already spent talking. All the audio "piles up" and gets processed as one block, even though the model could plausibly have started on the first sentence while you were still mid-way through the third.

The fix is voice activity detection (VAD): a lightweight classifier that looks at short audio frames (10–30ms chunks) and decides speech vs. silence, frame by frame. Once you have that running continuously during recording, you don't have to wait for the *manual* stop button to know a chunk of speech is finished — a long enough stretch of silence *after* speech is itself a signal that a sentence, or a thought, just ended.

I actually implemented this in the dictation tool: `webrtcvad` classifies audio frame by frame while recording; once a short-ish stretch of continuous silence follows a minimum amount of accumulated speech, that stretch gets cut into a segment and handed to a background worker thread, which transcribes and types it immediately — while the microphone keeps capturing whatever comes next. A small "pre-roll" buffer keeps the last few frames before speech was detected, so segments don't clip the first syllable. The practical effect: instead of one big blocking transcription at the end, you get several small ones streamed out while you're still talking, and the final manual stop just flushes whatever's left.

Notice what happened to trigger #2 (record-end): it didn't go away, it just multiplied. Instead of one manual end-of-recording signal, there are now many automatic end-of-*segment* signals nested inside one manual end-of-*session* signal. That distinction — one big trigger vs. many small ones — is going to come back.

## 3. From dictation to conversation: STT → LLM → TTS

Transcribing what you say is one thing; having something respond to it is another. The moment you add an LLM and a TTS step, the target usually shifts too — not just "type what I said" but "hold a spoken conversation," which raises the question of *where* this should run.

For anything privacy-conscious or bandwidth-constrained — think a small always-on box at home rather than a phone app calling out to the cloud — the appeal of doing STT and TTS locally is that only *text* needs to leave the device, if anything does at all, instead of raw audio. The catch is that a capable LLM is usually too heavy to run locally on that class of hardware (a Raspberry Pi, say). So the pipeline typically ends up split: STT, VAD, and TTS run on the edge device; the LLM call goes out to something bigger, local network or cloud, and only the token stream comes back.

Streaming becomes the thing that makes this tolerable rather than sluggish — but it doesn't apply symmetrically at every boundary. STT itself can run incrementally, transcribing continuously as audio comes in (the VAD-segmented approach from section 2 already does this), so the text for a chunk is ready almost the instant a pause is detected rather than only after a separate transcription pass starts from scratch. But the STT-to-LLM boundary isn't a streaming boundary — the LLM can't usefully start reasoning about a reply until it knows the person is actually done, since a partial utterance ("turn off the...") means something different depending on what comes next. That handoff is still gated by a discrete turn-completion trigger, the same kind from section 2, not by a stream of partial transcript.

The LLM-to-TTS boundary is where partial-output streaming genuinely applies, because it doesn't have that problem: once the LLM has generated the first few tokens of its reply, those tokens are fixed and won't be revised by whatever comes after, so TTS can start rendering and playing audio for the first sentence while the LLM is still generating the rest. A HuggingFace-style real-time voice setup is a reasonable concrete shape for the whole thing: VAD detects a pause, that pause triggers the LLM call, the response streams token by token, and TTS streams audio for those tokens as they arrive.

This is also where two more triggers show up that didn't exist in the dictation-only version: *when do we consider the transcript final enough to send to the LLM* (trigger #3), and *when do we start playing back TTS audio* — first sentence, or the whole response (trigger #4).

## 4. The real problem was never latency — it's knowing when someone is done talking

Here's where the pipeline from section 3, despite working correctly, starts to feel wrong. Silence-threshold VAD is a fine proxy for "did the sentence end" when someone is dictating a memo. It's a bad proxy for "did the *thought* end" when someone is thinking out loud — brainstorming with an LLM, working through a problem, pausing mid-sentence to figure out the next word. A fixed silence threshold either fires during that pause (interrupting a thought that wasn't finished) or, if you make it more patient, makes every *normal* exchange feel sluggish, because now it's waiting out the same generous window even when you clearly finished a quick question.

Tuning the threshold doesn't fix this, it just moves the discomfort around. The actual fix requires a different kind of signal: not *how long* was the silence, but *does what was said sound complete* — trailing conjunctions, unfinished clauses, rising intonation on a question that hasn't landed yet. That's a genuinely different mechanism from silence-VAD (sometimes called semantic or content-aware endpointing), and it costs something real: an extra inference call — a small classifier, or the LLM itself cheaply queried — every time a pause candidate shows up. You're trading compute for judgment.

This is worth naming as the actual thesis of the whole post: turn-taking is fundamentally a perception problem, not a latency problem. Silence duration is a crude, cheap proxy for something humans do constantly and mostly unconsciously, using cues (intonation, breath, filler words, even gaze in person) that raw audio silence simply doesn't carry.

Worth separating one thing before going further: how a conversation *starts* in the first place — a button press that opens a voice-chat session, or a wake word if you'd rather not touch anything — is a one-time activation decision. Everything below is the recurring, per-turn question of whether *this particular pause* means "I'm done." Easy to conflate, governed by completely different concerns. Once you're looking specifically at the per-turn question, it's worth cataloguing the actual space of ways a system can decide "now":

- **Manual button** — push-to-talk, push-to-interrupt, push-to-end. Zero ambiguity, all friction.
- **Silence-based VAD** — the baseline from section 2. Cheap, fast, blind to meaning.
- **Content/semantic endpointing** — judges completeness from what was said, not how long the pause was. More accurate, more expensive, needs its own inference call.
- **Speculative execution with a cancellation window** — fire a complete STT + LLM call on the flimsiest possible silence signal, run it in parallel with a much longer confirmation window, and throw it away if the person keeps talking before that window closes. Cheap to guess wrong, because unused LLM output costs compute but is never seen or heard. More on this below.
- **Hard timeout** — force an end after N seconds regardless, as a safety net under any of the above. Almost every shipped assistant has one.
- **Wake word** — used for initial activation, but also reusable as a narrow, low-false-accept trigger for barge-in (more on this in section 6).
- **Wait for the full response, then auto-restart listening** — the simplest possible turn-taking protocol: strictly alternating turns, automated. No barge-in, no overlap, but also nothing to get wrong.
- **System-initiated turns** — the system speaks *first*, unprompted, driven by a timer, sensor, or calendar event rather than any audio signal at all. A different direction entirely: not "did the user finish" but "does the system have something to say."
- **End-to-end learned turn-taking** — no separate classifier bolted onto a pipeline at all. The model is trained directly on full-duplex conversational audio and learns *when to speak* as part of itself, dissolving the whole taxonomy above into one learned behavior.

The speculative-execution item deserves a concrete example, because it's a genuinely clever piece of engineering. One real-time voice setup I looked at uses two silence thresholds instead of one: a very short one (32ms) fires a complete, real STT-plus-LLM call immediately — cheap, because the transcript is basically already sitting there ready. By their own account, once VAD detects speech they re-transcribe the whole growing buffer from scratch every 0.5 seconds while you're still talking — not a persistent streaming decoder, just Parakeet being fast enough (~30ms P50, 45ms P95, even at 15 seconds of audio) that redoing the whole thing repeatedly barely costs anything. So by the time the 32ms silence trigger fires, there's essentially nothing left to finalize, and the LLM call runs speculatively while a much longer window (on the order of a second) keeps counting. If you start talking again before that longer window closes, the whole in-flight response is discarded and the turn reopens; the transcription itself never stopped, so whatever you say next just extends the same growing transcript. Only if the long window elapses without further speech does the already-finished LLM response actually get spoken. The result: STT and LLM latency are almost entirely hidden inside a wait you were going to sit through anyway, and only text-to-speech's own startup cost is paid after the fact.

Picture it concretely: you say "Turn off the lights," pause for a beat — not because you're done, just breathing — and that beat alone is enough to cross the 32ms threshold. The system fires a real LLM call on exactly that much information and gets back something like "Which lights?" — a perfectly reasonable guess given what it had, and about to be wrong. You keep going: "...in the bedroom." Because you resumed within the grace window, "Which lights?" never gets used — it's discarded outright, and the transcript just keeps extending as if nothing had happened. A new speculative call fires on the next pause, this time against the full sentence, and comes back with "Bedroom lights off." Nothing interrupts the grace window this time, so it commits and gets spoken.

<iframe src="/assets/pipeline-animations/pipeline-speculative.html" width="100%" height="620" style="border:none; max-width:900px; display:block; margin:0 auto;" title="Step-through animation of the speculative-execution voice pipeline"></iframe>

*Click through the steps above: STT re-transcribes every half second regardless of pauses, the 32ms trigger fires a guessed reply, that guess gets discarded mid-flight, and a second attempt commits once a full second of clean silence elapses.*

It's worth being precise about what this technique does and doesn't fix. It's an optimization on *how cheaply and quickly* the system can act once a silence threshold is crossed — it doesn't change what that threshold is measuring. Underneath, it's still pure silence duration. A three-second pause in the middle of thinking out loud still eventually crosses the long threshold and gets a response shoved into it, exactly like plain single-threshold VAD would; it just got there via two clever steps instead of one. That's a different kind of fix than content/semantic endpointing, which actually looks at *what was said* rather than only how long the gap was — this technique makes the wrong decision cheaper to make, not less likely.

It's also worth separating three things that are easy to lump together as "streaming": whether audio *capture* is continuous, whether *transcription* is continuous, and whether the *send-to-LLM* decision is continuous or discrete. The setup above ends up continuous on all three in effect — but for transcription, not for the reason "continuous" usually implies. It's discrete batch transcription, fired on a fixed 0.5s clock while speech is ongoing, often enough to feel continuous — not a single persistent decoder holding state across the whole utterance. For utterances past 15 seconds they cap the growing cost the same way section 2 does: split into sentences and stop re-transcribing the ones already finished, only paying the "redo it all" cost for whichever sentence is still open. Structurally that's the same trick as VAD-segmenting a long recording — freeze what's done, keep paying only for the open piece — just applied at sentence granularity on a timer instead of at pause boundaries. I can confirm the same discrete-call reality on my own end directly: the Parakeet model I'm running locally, through `onnx-asr`, only exposes a single-shot `recognize(waveform)` call, no incremental decode API at all. Even that library's own built-in VAD integration is just "run VAD over a complete recording, then batch-transcribe each segment" — the same pattern built by hand in section 2. My own dictation tool is continuous capture, chunked transcription (one discrete STT call per VAD-closed segment, fired only at a detected pause rather than on a timer), and no automatic send-to-LLM decision at all, because it doesn't talk to an LLM — VAD there only decides when to transcribe, never when to act on the result.

All of that is clever engineering — and it never sat right with me for the thing I actually wanted this for: brainstorming out loud. So here's where I parted ways with it, and what I built instead.

That last distinction above is exactly why: for anything conversational, I'd personally keep the send-to-LLM decision manual rather than silence-driven at all — no threshold, however cleverly staged, tells the system "I'm still thinking" versus "I'm done" with any real confidence, and the failure mode (getting talked over mid-thought) is worse for a brainstorming partner than a slightly less snappy response time. Right now that means a dedicated key press to end a turn: VAD or continuous STT can still do useful work in the background (segmenting audio, keeping a transcript warm), but nothing gets sent to the LLM until I decide it should. A key isn't always available, though — talking to a robot from across a room, say — and there the same explicit-trigger principle would just move to a wake word or a short voice command instead of a silence timer. Either way it trades away the low-latency magic of the speculative approach for something more important in this use case: control over when I've actually finished a thought.

<iframe src="/assets/pipeline-animations/pipeline-steps.html" width="100%" height="700" style="border:none; max-width:900px; display:block; margin:0 auto;" title="Step-through animation of the explicit-trigger voice pipeline"></iframe>

*Same automatic VAD-driven audio chunking as before, but no threshold — short, long, or two of them staged together — ever triggers the LLM on its own. Only a deliberate key press does, with one more transcription pass catching up right after.*

None of these is "the" answer. Which one is right depends entirely on what you're building — a point worth holding onto for the closing section.

## 5. Conversations end too: history and session boundaries

Everything above operates on a scale of milliseconds to seconds — is this pause over, should I answer now. There's a different kind of trigger operating on a completely different timescale: is this still the *same conversation*, or has a new one started.

Multi-turn conversation needs some memory of prior turns to make sense of follow-ups ("what about the second one" only means something if the model remembers what "the second one" refers to). But that context can't just grow forever — cost, latency, and eventually the context window itself all push back. And an unbounded, never-reset history creates its own failure mode: old context bleeding into requests it has nothing to do with, like a "continue the story" instruction lingering into an unrelated "turn off the lights."

So this needs its own trigger, distinct from turn-taking within a conversation: when do we decide *this conversation is over* and the next utterance should start from a clean slate? Options mirror some of the same shapes as before — an explicit signal (user says "new topic," or presses a button), a long silence or absence (they walked away), a hard timeout since the last exchange — plus a middle ground that's specific to this problem: summarizing and carrying forward a compressed version of old turns instead of either keeping everything or dropping everything. It's a state-management problem more than a latency problem, but it belongs in the same family as the rest: it's still fundamentally a decision about *when* to act differently, just at the scale of minutes or topic shifts instead of milliseconds.

## 6. Barge-in: when the assistant needs to shut up

A response that's too long, or wrong, or beside the point deserves to be interrupted — the way a normal conversation actually works. That requires the mic to stay meaningfully usable *while the speaker is also playing audio*, which naively just means the mic hears itself: an echo problem.

It's worth separating two distinct failure modes here, because they call for different fixes:

1. **Content collision** — the exact phrase you're listening for (say, a wake word) happens to appear in the TTS output itself. Rare, and since you know your own TTS script exactly, you can even suppress detection during the specific window where you know that phrase is about to be spoken.
2. **Acoustic masking** — even audio that has nothing to do with the trigger phrase raises the noise floor at the mic and can bury real speech underneath it, independent of content. This is the actual reason real devices (Echo, Google Home) run acoustic echo cancellation (AEC) even though they only need a narrow wake-word trigger for barge-in — AEC isn't there to stop the device recognizing its own voice, it's there to keep the mic's signal-to-noise ratio usable at all while the speaker is loud.

A pragmatic first iteration doesn't need full AEC hardware to get *some* barge-in working. Swap continuous general VAD/ASR for a narrow wake-word detector as the open-mic listener during playback. A keyword spotter has a much smaller false-accept surface than a general speech classifier, so it tolerates a meaningful amount of acoustic leakage on its own — especially at moderate volume or distance. Real AEC then becomes the refinement for loud, close-coupled setups (a robot's own speaker sitting right next to its own mic, say), not a hard prerequisite for barge-in to exist at all. It's the same shape of staging as the VAD segmentation change in section 2: ship the simpler mechanism first, add the harder one when the simple one's limits actually show up. One more practical wrinkle worth knowing about regardless of approach: stopping playback on interrupt isn't instantaneous, since audio already handed to the speaker/DAC keeps playing for a moment — there's always a small residual tail.

Purpose-built hardware (mic/speaker arrays designed specifically around this problem, like the Reachy Mini robot) exists precisely because getting this right in general — loud, close-range, real-time — genuinely does need acoustic engineering, not just software.

## 7. Always responsive, not always recording: wake words

Sitting in front of everything above is one more gate: how do you make a device feel "always listening" without either streaming raw audio anywhere continuously, or burning meaningful power running a full STT model around the clock?

Small, efficient, on-device keyword-spotting models solve this — they're a fraction of the size and cost of a full STT model, continuously classifying only for a narrow trigger phrase, and only waking the heavier pipeline (VAD, STT, LLM, TTS) once that phrase is detected. This is also the mechanism that makes "not always listening" a meaningful, honest claim rather than a marketing line — the mic being physically on is not the same thing as anything being transcribed, stored, or sent anywhere.

## 8. When speech isn't even the right output

Not every context wants a spoken answer back. Sitting at a laptop, reading is usually just faster than listening — the output modality itself is a decision the system could make, or let the user toggle, not a given default. And even when speech is the right call, playback speed is its own small technical trap: simply speeding up audio raises its pitch (the chipmunk effect), so a genuinely useful "listen faster" feature needs proper time-stretching that decouples speed from pitch, not just a naive playback-rate change.

## Closing: no ideal setup found yet

Here's the honest state of things, at least from where I'm standing: a simple VAD-threshold rule feels too trigger-happy the moment real thinking pauses are involved — brainstorming, working through a problem out loud. The fix (a smarter, content-aware, possibly LLM-assisted listener) trades that discomfort away for real cost and complexity, and it's not obviously worth it for every use case.

Which is really the point — "best" depends entirely on what's being built. Three concrete use cases sit at genuinely different points on this tradeoff space:

- **A privacy-respecting home assistant** (an Alexa alternative with more control over what leaves the device) cares most about wake-word gating and system-initiated turns — the "when" that matters most is rarely mid-conversation timing, it's "can I trust this thing to actually be off when I think it's off."
- **An LLM as a brainstorming or thinking partner** cares most about *not* interrupting during pauses — tolerant of, even wanting, a much more patient or content-aware endpointing strategy, since the cost of a premature interruption is far higher than the cost of a slightly slower reply.
- **Robot control** cares most about barge-in and low end-to-end latency — a robot mid-action needs to be interruptible immediately, for reasons that go beyond convenience into safety.

Worth ending on the frontier attempt to sidestep this whole taxonomy rather than tune it: end-to-end learned turn-taking, where the model is trained on full-duplex conversational audio and learns when to speak as part of itself, rather than having a separate classifier bolted onto a modular pipeline. It's the closest thing to "solved" that exists right now — but it's a different paradigm, not obviously a strictly better one for every use case above, and it's fair to leave that question open rather than pretend there's a clean answer yet.
