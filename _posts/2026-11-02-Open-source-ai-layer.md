---
layout: post
title: "The open-source AI layer nobody talks about"
date: 2026-11-02
---
While everyone's watching the LLM race, another huge leap just happened — and hardly anyone is talking about it.

Whenever AI comes up, the spotlight is almost always on the big LLMs and VLMs — Claude, GPT, Gemini. They are API-only, which makes them a real dependency. What gets a lot less attention: there's an entire other layer of AI making just as much progress — time series forecasting, computer vision (object detection, OCR, instance segmentation...), speech recognition, speech synthesis. And the models in this layer aren't just getting better, they're getting dramatically more efficient. Efficient enough to run locally, mostly without a GPU — and mostly open source.

I've been building a handful of small side projects over the past months on exactly this layer — parsing documents, transcribing podcasts, talking to an AI assistant by voice, forecasting time series, making a photo and video library searchable — and the common thread is: almost none of it needs the cloud. Mostly on CPU, with specialized open models that are each really good at one narrow thing.

## Four domains, one theme: small, specialized, open

**Documents: from scans to a searchable knowledge base.** Dewarp the page with UVDoc, detect layout and reading order and run OCR with PaddleOCR, then embed text and images into one searchable space with EmbeddingGemma 2. A messy scan becomes a searchable, structured document, all local. My pipeline: [local-ocr-processing](https://github.com/cgroll/local-ocr-processing)

**Speech: from podcasts to a push-to-talk assistant.** Parakeet transcribes a single speaker; add Sortformer for speaker diarization and a podcast recording turns into "who said what, when." For talking to an AI assistant, I use Parakeet (speech-to-text) and Phonon (text-to-speech) in a push-to-talk setup. That lets me think out loud, pause mid-sentence, and get answers read back to me — including over a Telegram bot while walking, where typing isn't an option anyway. My projects: [conversation-transcriptor](https://github.com/cgroll/conversation-transcriptor) and [speech-to-speech](https://github.com/cgroll/speech-to-speech)

**Time series: forecasting out of the box.** Mistral's time series foundation model gives solid zero-shot forecasts. I've used it for smaller problems like load forecasting, with no task-specific training required.

**Vision: photos and video, searchable.** EmbeddingGemma 2 turns a photo library into a semantic search index ("Las Vegas," "portrait of a laughing boy") — no tags required. Combined with speech-to-text, the same idea makes video libraries searchable too. For faces, detection plus ArcFace embeddings handle recognition; for everything else, YOLO, RF-DETR, SAM3, and Depth Anything v3 cover detection, segmentation, and depth. My project for video search: [offline-video-understanding](https://github.com/cgroll/offline-video-understanding)

## Try it yourself

None of these models is flashy on its own. Chained together, they add up to a genuinely capable, fully local AI stack: documents, speech, time series, vision — all running locally, mostly on CPU, and all open source.
