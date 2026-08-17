# /// script
# dependencies = ["edge-tts"]
# ///
import asyncio
import json
import re
from pathlib import Path

import edge_tts

HERE = Path(__file__).parent
VOICE = "en-US-GuyNeural"

# Reused verbatim from the first prototype (post 1) — same animation, same narration.
ANIM1_STEPS = [
    "Here's what that looks like under the hood. You start speaking, and speech-to-text starts re-transcribing everything every half second — not waiting for a pause, just running on a fixed clock.",
    "You pause. Just thirty-two milliseconds of silence — far shorter than a real pause needs to be.",
    "But that's already enough to fire a speculative reply, based on whatever's been said so far.",
    "You keep talking. The grace window was still open, so that's allowed.",
    "The speculative reply gets thrown away — but the transcript never stopped. Only the guess was wasted.",
    "A real pause. Thirty-two milliseconds fires again.",
    "A new speculative reply fires immediately, this time based on the full sentence.",
    "Nothing interrupts it. A full second of silence passes, uninterrupted.",
    "The gate opens. The reply was already sitting there, ready.",
    "Speech starts almost immediately — because the LLM's answer was already there, waiting, and now it streams straight into text-to-speech too.",
]

# Adapted from pipeline-steps.html's own step headlines/subtext into spoken narration.
ANIM2_STEPS = [
    "Here's how that actually works. You start speaking.",
    "You pause. VAD notices — a chunk boundary gets marked and the transcription starts with the existing audio.",
    "You keep talking, while that first chunk finishes transcribing in the background — speech-to-text always lags a little behind.",
    "You decide you're done, and press send — no VAD needed here. The manual trigger fires on its own, whether or not a pause was ever detected. Which means you can record audio with pauses built right into it — exactly what happens to me when I'm still sorting out my thoughts, using an AI agent as a sparring partner.",
    "One more transcription to catch up on — the last stretch of audio still has to go through speech-to-text before anything can be sent.",
    "Both chunks arrive at the LLM together.",
    "The reply starts streaming. First token out — but nothing's spoken yet, text-to-speech needs a little buffer before it can start.",
    "Speech catches up, one token behind.",
    "Streaming continues, still one step behind.",
    "And the last word is spoken. No more tokens coming — text-to-speech just finishes what it already has.",
]

ANIM3_STEPS = [
    "Audio comes in as a stream, cut into fixed-size chunks.",
    "A second chunk arrives, still no transcript yet.",
    "Two chunks in, and the first transcript catches up — transcribing them took about as long as this third chunk took to arrive.",
    "A fourth chunk comes in, same story.",
    "The second transcript catches up too. The fifth chunk is still just audio — nobody's transcribed it yet, because you're still speaking.",
]

USECASE_ITEMS = [
    "Brainstorming on a walk",
    "Speaking instructions while vibe-coding",
    "Steering a robot — no keyboard to type on",
]
USECASE_TEXTS = [
    "Brainstorming out loud, on a walk.",
    "Speaking instructions instead of typing them, while you're vibe-coding.",
    "Or steering a robot — where there's no keyboard to type on in the first place.",
]

SCENES = [
    {"id": 1, "text": "Talking to an AI can be genuinely powerful.", "visual": {"kind": "text_slide", "style": "statement", "content": "Talking to an AI can be\ngenuinely powerful."}},
]

for _i, _line in enumerate(USECASE_TEXTS, start=1):
    SCENES.append({
        "id": 1 + _i,
        "text": _line,
        "visual": {"kind": "checklist_step", "group": "usecases", "kicker": "USE CASES", "items": USECASE_ITEMS, "step": _i},
    })

SCENES += [
    {"id": 5, "text": "And speech-to-speech is actually simple to build: speech-to-text, an LLM as the agent in the middle, text-to-speech. Three models, stitched together.", "visual": {"kind": "text_slide", "style": "pipeline-basic"}},
    {"id": 6, "text": "This already exists as a streaming API you can just call — Google's Streaming API, OpenAI's Realtime API.", "visual": {"kind": "text_slide", "style": "statement", "content": "This already exists as a streaming API\nyou can just call."}},
    {"id": 7, "text": "But there's a catch: you're sending raw audio back and forth, and you don't have full control over the agent sitting in the middle.", "visual": {"kind": "text_slide", "style": "pipeline-cloud"}},
    {"id": 8, "text": "The alternative: run speech-to-text and text-to-speech locally. Only text ever leaves the device.", "visual": {"kind": "text_slide", "style": "pipeline-local"}},
    {"id": 9, "text": "But now, if you want it to actually feel good to use, a lot of that logic is on you. Luckily, Huggingface already did the work and open-sourced a reference build — there's a lot to learn about what a good user experience actually takes, just from looking closely at it.", "visual": {"kind": "text_slide", "style": "statement", "content": "A lot of that logic\nis on you."}},
    {"id": 10, "text": "We need one more component for a smooth pipeline: voice activity detection, or VAD. It's a lightweight classifier that listens to the audio and flags when a stretch of silence looks like a pause.", "visual": {"kind": "text_slide", "style": "pause"}},
    {"id": 11, "text": "And that brings us to the first problem: latency. Wait for one big block of audio, and transcription only starts once you're already done talking. Huggingface solves this part without even needing VAD.", "visual": {"kind": "text_slide", "style": "statement", "content": "Wait for one big block of audio,\nand you're staring at silence."}},
    {"id": 12, "text": "So instead: chunk it, and keep re-transcribing in the background while you're still speaking.", "visual": {"kind": "text_slide", "style": "statement", "content": "So instead: chunk it,\nkeep re-transcribing in the background."}},
]

for _i, _line in enumerate(ANIM3_STEPS, start=1):
    SCENES.append({
        "id": 12 + _i,
        "text": _line,
        "visual": {"kind": "animation_step", "group": "chunk_transcribe", "anim_step": _i},
    })

SCENES += [
    {"id": 18, "text": "Now that speech-to-text is fast, we also need the LLM's response to be fast. That's where Huggingface uses a smart trick — and this is where VAD actually comes in.", "visual": {"kind": "text_slide", "style": "statement", "content": "Now the LLM needs to be fast too.\nThis is where VAD actually comes in."}},
]

for _i, _line in enumerate(ANIM1_STEPS, start=1):
    SCENES.append({
        "id": 18 + _i,
        "text": _line,
        "visual": {"kind": "animation_step", "group": "pipeline_speculative", "anim_step": _i},
    })

SCENES += [
    {"id": 29, "text": "And the very last piece: don't wait for the LLM's full reply either. Stream tokens straight into text-to-speech as they're generated.", "visual": {"kind": "text_slide", "style": "statement", "content": "Don't wait for the full reply either.\nStream tokens straight into speech."}},
    {"id": 30, "text": "That's the Huggingface real-time pipeline — and for this use case, it's genuinely great UX: a fast, low-latency conversation. But it's a bad fit for long pauses, for actually thinking out loud — and that's often exactly my use case.", "visual": {"kind": "text_slide", "style": "thesis", "kicker": "HUGGINGFACE REAL-TIME PIPELINE", "content": "Fast conversation.\nBad for thinking out loud."}},
    {"id": 31, "text": "So here's the alternative I actually use instead: I manually decide when to hand the turn over — and I run my own, personal agent in the middle, rather than a general-purpose one.", "visual": {"kind": "text_slide", "style": "statement", "content": "I manually decide when to hand the turn over —\nand run my own agent, not a general-purpose one."}},
]

for _i, _line in enumerate(ANIM2_STEPS, start=1):
    SCENES.append({
        "id": 31 + _i,
        "text": _line,
        "visual": {"kind": "animation_step", "group": "pipeline_steps", "anim_step": _i},
    })

SCENES += [
    {"id": 42, "text": "For the best experience, you need a bit more logic still — take wake word detection, for example. It's a small, always-on model listening for nothing but a single trigger phrase — \"Hey Google,\" \"Alexa\" — cheap enough to run continuously, without waking the rest of the pipeline.", "visual": {"kind": "text_slide", "style": "wakeword"}},
    {"id": 43, "text": "Then there's barge-in: interrupting the reply before it's finished. You need a signal for that.", "visual": {"kind": "text_slide", "style": "bargein-interrupt"}},
    {"id": 44, "text": "The easy way is a push button — press it, and the assistant stops talking.", "visual": {"kind": "text_slide", "style": "bargein-button"}},
    {"id": 45, "text": "Otherwise, the signal is just you speaking again. But that means detecting your voice while the speaker is still playing the reply back — harder than it sounds.", "visual": {"kind": "text_slide", "style": "echo-overlap"}},
    {"id": 46, "text": "On headphones, that's not a problem. Without them, you need real acoustic echo cancellation hardware.", "visual": {"kind": "text_slide", "style": "echo-compare"}},
    {"id": 47, "text": "Or you sidestep the echo problem entirely: use a wake word again, so the assistant can tell your voice apart from its own.", "visual": {"kind": "text_slide", "style": "wakeword-mini"}},
    {"id": 48, "text": "After building something like this myself, I ended up writing the whole walkthrough down — partly just so I could keep the current logic straight in my own head. It's all there in detail, in text, on my blog.", "visual": {"kind": "text_slide", "style": "statement", "content": "I wrote the whole walkthrough down."}},
    {"id": 49, "text": "It contains a full writeup and the interactive walkthroughs — link in the comments.", "visual": {"kind": "text_slide", "style": "cta", "content": "quantitative-thinking.com"}},
]


def words_of(text: str) -> list[str]:
    return text.split()


def has_alnum(token: str) -> bool:
    return bool(re.search(r"[A-Za-z0-9]", token))


async def synthesize(full_text: str, out_mp3: Path) -> list[dict]:
    communicate = edge_tts.Communicate(full_text, VOICE, boundary="WordBoundary")
    boundaries = []
    with open(out_mp3, "wb") as f:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                f.write(chunk["data"])
            elif chunk["type"] == "WordBoundary":
                boundaries.append(chunk)
    return boundaries


def main():
    full_text = " ".join(s["text"] for s in SCENES)
    out_mp3 = HERE / "audio" / "narration_v3.mp3"
    boundaries = asyncio.run(synthesize(full_text, out_mp3))

    print(f"Total scenes: {len(SCENES)}")
    print(f"Total boundary events: {len(boundaries)}")

    cursor = 0
    timings = []
    for scene in SCENES:
        expected = words_of(scene["text"])
        spoken = [w for w in expected if has_alnum(w)]
        n = len(spoken)
        if n == 0:
            timings.append({"id": scene["id"], "start": timings[-1]["end"] if timings else 0.0, "end": timings[-1]["end"] if timings else 0.0})
            continue
        chunk = boundaries[cursor: cursor + n]
        if len(chunk) != n:
            raise RuntimeError(
                f"Scene {scene['id']}: expected {n} spoken words, only {len(chunk)} boundaries left. "
                f"Expected={spoken} Got={[b['text'] for b in chunk]}"
            )
        start = chunk[0]["offset"] / 1e7
        end = (chunk[-1]["offset"] + chunk[-1]["duration"]) / 1e7
        timings.append({"id": scene["id"], "start": start, "end": end})
        cursor += n

    if cursor != len(boundaries):
        print(f"WARNING: consumed {cursor} boundaries but {len(boundaries)} were produced")

    display = []
    for i, t in enumerate(timings):
        scene_start = t["start"]
        if i + 1 < len(timings):
            scene_end = timings[i + 1]["start"]
        else:
            scene_end = t["end"] + 1.2
        display.append({"id": t["id"], "start": round(scene_start, 3), "end": round(scene_end, 3), "duration": round(scene_end - scene_start, 3)})

    print("\nPer-scene timing (first 5, last 5):")
    for d in display[:5]:
        print(d)
    print("...")
    for d in display[-5:]:
        print(d)

    total_audio_end = timings[-1]["end"]
    print(f"\nTotal narration length (last word end): {total_audio_end:.2f}s")

    out = {"scenes": SCENES, "timing": display, "audio_file": str(out_mp3), "total_seconds": total_audio_end + 1.2}
    (HERE / "scene_timing_v3.json").write_text(json.dumps(out, indent=2))
    print(f"\nWrote {HERE / 'scene_timing_v3.json'}")


if __name__ == "__main__":
    main()
