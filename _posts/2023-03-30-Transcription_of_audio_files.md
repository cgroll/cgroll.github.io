---
layout: post
title:  "Building a data science product with python: Transcription of audio conversations"
date:   2023-03-30
categories: [AI, Tools]
excerpt: > #
  Link to a video series that shows how to automatically transcribe mp3/wav podcasts with python using whisper and pyannote.
math: false
---

I created a video series that shows how one can combine [Open AI's
whisper model](https://openai.com/research/whisper) and the [pyannote
speaker diarization python
package](https://github.com/pyannote/pyannote-audio) in order to
create a tool to automatically transcribe audio conversations.

<br>

The tool is based on a pretty simplistic heuristic that combines
speech-to-text from whisper and speaker diarization from pyannote.
There are already some services on the internet that offer similar
applications. However, I was first of all just curious about the
capabilities of whisper when I first heard about it. And second, I
just did not want to sign up for yet another paid subscription
service ;-)

<br>

Also, I thought it would be a pretty good use case for another project
that I always wanted to do: record a tutorial series on how to build a
data science product. Based on my experiences in the industry, there
is so much more to a data science product than just the model
development part. That's why I wanted to put some spotlight also on
the software engineering part (tools and best practices like IDE, git,
CI, cookiecutter, testing, ...) as well as on the thought processes
behind the structuring of code and APIs of functions.

<br>

In addition, I wanted to approach the task also from the product side.
Once you have implemented a tool that you deem worthwhile to share,
you need to ask yourself how you want to do this. Do you want to share
it as a python package? But then usage will be limited to people that
know how to install python code and dependencies (including
potentially required system libraries). Or do you intend to make it
accessible in the cloud through a simple web browser? And how could
you monetize your product?

<br>

By the time of writing, I'm not fully finished yet with all components
that I originally wanted to record. But since I'm pretty busy with
other projects at the moment as well, I thought I'd already share the
videos that are already done and gradually keep adding new ones
whenever I find the time.

<br>

<iframe width="560" height="315" src="https://www.youtube.com/embed/aiFUJU-dXhI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>