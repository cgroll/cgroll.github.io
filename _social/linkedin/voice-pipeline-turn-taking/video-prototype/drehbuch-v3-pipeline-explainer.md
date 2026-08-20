Drehbuch v3 — "Wie man Speech-to-Speech wirklich baut" (Mini-Erklärvideo)
Roter Faden: Use Cases -> naive Architektur -> Streaming-API-Falle -> lokale Alternative ->
zwei Latenz-Probleme -> Speculative-Execution-Lösung (bestehende Animation) -> Tradeoff ->
mein Ansatz: expliziter Trigger (bestehende Animation) -> Teaser

Legende: [NEU] = neue Visual nötig, [REUSE] = bestehende Animation/Element wiederverwendet

---

TEIL A — Hook: Use Cases

1. "Talking to an AI can be genuinely powerful."
   [NEU] Statement-Slide

2. "Brainstorming out loud, on a walk."
3. "Speaking instructions instead of typing them, while you're vibe-coding."
4. "Or steering a robot — where there's no keyboard to type on in the first place."
   [NEU] Drei kurze Statement-Slides, evtl. mit kleinem Icon pro Use Case (Fußgänger/Spaziergang,
   Tastatur-durchgestrichen, Roboter) — oder als eine Szene mit 3 Zeilen, die nacheinander einfliegen
   (wie die Checklist-Animation aus Post 1, gleiche Technik wiederverwendbar)

---

TEIL B — Die einfache Architektur

5. "And speech-to-speech is actually simple to build: speech-to-text, an LLM as the agent
    in the middle, text-to-speech. Three models, stitched together."
   [NEU] Einfaches 3-Boxen-Diagramm: STT -> LLM (AGENT) -> TTS, mit Pfeilen dazwischen.
   Farben passend zur bestehenden Palette (STT/TTS teal, LLM lila).

---

TEIL C — Streaming-APIs und ihr Haken

6. "This already exists as a streaming API you can just call — Google's Streaming API,
    OpenAI's Realtime API."
7. "But there's a catch: you're sending raw audio back and forth."
8. "And you don't have full control over the agent sitting in the middle."
   [NEU] Statement-Slides, evtl. Variante des 3-Boxen-Diagramms mit einer Cloud-Markierung
   um LLM+Audio-Pfeile, um "das läuft extern, roher Audio-Strom" zu visualisieren

---

TEIL D — Lokale Alternative und ihr Preis

9. "The alternative: run speech-to-text and text-to-speech locally. Only text ever
    leaves the device."
10. "But now, if you want it to actually feel good to use, a lot of that logic is on you.
    That's exactly what I found looking at Huggingface's reference build."
   [NEU] Statement-Slide, evtl. das 3-Boxen-Diagramm nochmal mit STT/TTS "auf dem Gerät"
   markiert (kleines Device-Icon) und nur ein Text-Pfeil zum LLM

---

TEIL E — Problem 1: Wann ist die Eingabe fertig?

11. "First problem: when is someone actually done talking? That's voice activity
    detection — VAD."
   [NEU] Statement/kurze Erklär-Slide (evtl. Pause-Visual aus Post 1 wiederverwendbar: Silent-Bars + VAD-Marker)
   [REUSE] Pause-Stil aus Post 1 (VAD-Marker + Silent-Bars)

---

TEIL F — Problem 2: Latency / Pile-up

12. "Second problem: latency. Wait for one big block of audio, and transcription only
    starts once you're already done talking."
13. "So instead: chunk it, and keep re-transcribing in the background while you're
    still speaking."
   [NEU] Statement-Slides — das Pile-up-Problem selbst braucht wahrscheinlich kein eigenes
   Diagramm, wird durch die folgende Animation ohnehin gezeigt (dort re-transkribiert STT
   ja bereits "every 0.5s" im Hintergrund)

---

TEIL G — Immer noch Latency: Grace Window statt voller Stille

14. "Still not fast enough. Waiting out a full silence costs real time — so instead of
    waiting, fire early, on the flimsiest pause you can get away with."
   [REUSE] Ab hier: komplette pipeline-speculative.html Animation, alle 10 Schritte,
   mit eigenem Sprechtext pro Schritt (wie in Post 1 schon gebaut — Text kann fast 1:1
   aus Post 1 übernommen werden, ggf. leicht gekürzt)

---

TEIL H — Letztes Puzzleteil: Token-Streaming in TTS

15. "And the very last piece: don't wait for the LLM's full reply either. Stream tokens
    straight into text-to-speech as they're generated."
   [NEU] Statement-Slide (Übergang), Diagramm-Idee optional: kleine Token-Kette mit Pfeil zu TTS

---

TEIL I — Der Tradeoff

16. "The result: low latency, a fast back-and-forth conversation."
17. "But a bad fit for long pauses — for actually thinking out loud."
   [NEU] Zweifarbige These-Slide, gleicher Stil wie "Not latency. Perception." aus Post 1:
   Zeile 1 grün/neutral ("Fast conversation."), Zeile 2 in Warnfarbe ("Bad for thinking out loud.")

---

TEIL J — Die Alternative: Expliziter Trigger

18. "So here's the alternative I actually use: I decide when to hand the turn over."
   [NEU] Statement-Slide

19. "VAD still chunks the transcript in the background — real pauses, not tiny ones,
    so nothing piles up."
20. "But nothing goes to the LLM until I press a button."
21. "The reply still streams straight into speech, token by token."
   [REUSE] Ab hier: komplette pipeline-steps.html Animation, alle 10 Schritte, eigener
   Sprechtext pro Schritt (Struktur exakt wie bei pipeline-speculative in Teil G)

---

TEIL K — Teaser / Ende

22. "There's more still — barge-in, wake words, knowing when a conversation itself is
    over. More on that soon."
23. "Full writeup and both interactive walkthroughs — link in the comments."
   [REUSE] Teaser- und CTA-Stil aus Post 1, unverändert übernehmbar

---

STATUS:

3. GEKLÄRT (2026-08-10): Kein Bezug zu einem LinkedIn-Post — eigenständiges Erklärvideo zum
   Thema, unabhängig von der Post-Serie. "Post 1" oben bezeichnet nur weiterhin die Quelle für
   wiederverwendbaren Slide-Stil/Technik (Checklist-Animation, Thesis-Slide, Teaser/CTA-Look),
   nicht eine Abfolge, die dieses Video ersetzt oder fortsetzt.

OFFENE FRAGEN (noch unbeantwortet):

1. Neue Visuals: Teil B/C/D brauchen ein neues 3-Boxen-Pipeline-Diagramm (STT/LLM/TTS),
   in 2-3 Varianten (Basis, "Cloud/Audio", "lokal/Text"). Das ist die einzige wirklich neue
   Grafik-Arbeit in diesem Drehbuch — alles andere ist Wiederverwendung aus dem bisherigen
   Slide-Stil bzw. den beiden bestehenden Animationen.

2. Länge: 23 Beats, davon 20 Schritte aus den zwei bestehenden Animationen (je 10) —
   grobe Schätzung 3-6s pro Beat je nach Textlänge => vermutlich 130-160s Gesamtlänge.
   Deutlich länger als das erste Prototyp-Video. Ist das noch im Rahmen, oder splitten wir
   in zwei Teile (z.B. Teil A-I als ein Video, Teil J-K als zweites)?
