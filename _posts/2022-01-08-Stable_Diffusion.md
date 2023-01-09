---
layout: post
title:  "Stable Diffusion"
date:   2022-01-08
categories: [Tools, HowTo]
excerpt: > #
  Get your coding and data science skills pumped up with workshops and
  publicly available lesson material of the Carpentries. Amongst
  others, learn how to use Unix Shell, Git, scientific computing
  languages (Python, R, Matlab), SQL, Make and Webscraping.
math: false
---

I finally managed to play around with text-to-image AI models. I used Stable Diffusion. Installed it locally in order to benefit from my GPU setup. But you actually can play around with it pretty nicely in your browser as well. Here are the most important HuggingFace spaces for this:

### Image from text

HuggingFace space: [stabilityai/stable-diffusion-1](https://huggingface.co/spaces/stabilityai/stable-diffusion-1)

There are some google example prompts already. As it turns out a good prompt is actually not that easy to create. Luckily there are couple of pages that list good examples. I took two examples from [Best 100 stable diffusion prompts](https://mpost.io/best-100-stable-diffusion-prompts-the-most-beautiful-ai-text-to-image-prompts/). Another great web page to help you create a good prompt is [Lexica](https://lexica.art/).

<br>


The first prompt that I tried was:

<br>


```
portrait photo of a asia old warrior chief, tribal panther make up, blue on red, side profile, looking away, serious eyes, 50mm portrait photography, hard rim lighting photography–beta –ar 2:3 –beta –upbeta –upbeta
```

<br>

It gave me some really impressive photorealistic images:

<br>


<p align="center">
  <img src="/assets/images/stable_diffusion_warrior_chief.jpeg" alt="Warrior chief" width="500"/>
</p>

<br>

The second prompt that I tried was less photorealistic and more of a Pixar movie art:

<br>


```
glowwave portrait of curly orange haired mad scientist man from borderlands 3, au naturel, hyper detailed, digital art, trending in artstation, cinematic lighting, studio quality, smooth render, unreal engine 5 rendered, octane rendered, art style by pixar dreamworks warner bros disney riot games and overwatch.
```

<br>

It created some pretty impressive mad scientist images:

<br>

<p align="center">
  <img src="/assets/images/stable_diffusion_mad_scientist.jpeg" alt="Mad scientist" width="500"/>
</p>

<br>

### Image from text, including negative prompt

HuggingFace space: [stabilityai/stable-diffusion](https://huggingface.co/spaces/stabilityai/stable-diffusion)

Here you can additionally specify things that should not be displayed. For example, you can use it to create a warrior chief without feathers.

<br>

<p align="center">
  <img src="/assets/images/stable_diffusion_warrior_chief_no_feathers.png" alt="Warrior chief without feathers" width="500"/>
</p>

<br>


### Image inpainting

HuggingFace space: [multimodalart/stable-diffusion-inpainting](https://huggingface.co/spaces/multimodalart/stable-diffusion-inpainting)

<p align="center">
  <img src="/assets/images/stable_diffusion_inpainting.png" alt="Warrior chief with modified face painting" width="500"/>
</p>


### Own experiment

<p align="center">
  <img src="/assets/images/stable_diffusion_giraffe_elephant.png" alt="Elephant with giraffe spot pattern" width="500"/>
</p>
