---
layout: post
title: "What does it take to become an AI nation? The layers, the bottlenecks, and a view from Europe"
date: 2026-11-18
---
When people ask "what does it take to make AI work?", they usually think of one company: a model, a chat window, a project. This text asks a different question: **what does it take for a country or a region to make AI work?** A single company will not build a data center or a chip factory. A state, or a continent, has to think about all of it.

## 1. The layers

**Applications.** Where AI meets a use case. A chat window alone is not enough: the AI has to be connected to an organization's own data (access rights, retrieval, workflows).

**Foundation models.** The model itself. To build it, you need data, research knowledge and the people who have it, and a very large amount of compute.

**Inference and operations.** Not everyone needs to build their own model. In many domains there are great foundation models that you could use without further fine-tuning. But regardless of where the models come from, you want to run them reliably, quickly and cheaply at scale. This is its own discipline, separate from model training.

**Data centers and hardware.** Chips, memory, networking, cabling, and power. And of course, the raw materials and the manufacturing chain sit behind all of this hardware.

## 2. Where the bottlenecks are

Having all layers on paper is not enough. Things can get stuck:

- **Power.** Data centers need a lot of electricity, and grid connections and build times limit how fast capacity can come online.
- **Compute.** Chips and memory are scarce, and the hardware has to be bought sensibly.
- **Cost.** Cheap data center operation, fast inference and sensibly bought hardware together make up the cost of AI. If it is too expensive, good use cases stay unused.
- **Know-how.** Research talent for models, and operations skills for running them well.

The goal is that once good use cases exist, none of these holds anyone back.

## 3. A view from Europe: what to prioritize

Applied to Europe, the question becomes one of order. Full sovereignty means covering every layer, and that is not realistic all at once, at least in the short term. Europe already runs largely on the data centers of the hyperscalers, and there is no point in pretending otherwise. A sensible order:

**1. Make the use cases deliver real value.** First priority is the application layer: use cases that people actually want, with AI embedded in an organization's own data. This works even while the layers below stay dependent.

Not only large language models: the application layer is not only about big LLMs and vision-language models. Much of the practical value sits elsewhere: computer vision, speech recognition, and time-series foundation models for sensors, machines and forecasting. These are often smaller and cheaper to run. A view that only looks at large chat models is too narrow.

**2. Make sure there is no bottleneck.** Once good use cases exist, there must be enough power and compute to serve them. Power could become a disadvantage in Europe: energy is comparatively expensive, and grid connections and build times are slow. Keeping AI cost-efficient on European soil belongs here.

**3. Reduce dependencies, last.** Only then does it make sense to work on independence: first open-weight models (cheaper, and more independent), then own foundation models, and finally own hardware.

Full independence across every layer is the right long-term goal. But where Europe stands today, the better question is which steps create value now and make the next ones easier.
