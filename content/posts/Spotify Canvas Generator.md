---
title: Spotify Canvas Generator
date: 2024-12-31
draft: false
---

I've been working on some new music and wanted to have a way to create a [Spotify Canvas](https://artists.spotify.com/canvas) from my album artwork. This script needed to do a [few things](https://support.spotify.com/us/artists/article/canvas-guidelines/):

- Take album artwork as input (or any still image)
- Resize to 9:16 for phone screens
- Apply the effect(s)
	- random digital artifacting
	- glitches from the `glitch-this` library
	- vertical pixel smearing
- output a few different filetypes in a new directory: 
	- png 
	- gif 
	- final mp4 for spotify

Here's an example with the album artwork:

### Original

![Image Description](/images/my-mind-cover1.jpg)

### Spotify Canvas

![Image Description](/images/my-mind_canvas1.gif)

Boom.

Feel free to check out the code and the music! Repo linked [here](https://github.com/danialrami/canvas-generator_spotify). The python is open-sourced, so feel free to use, edit, copy, or anything else. Try some different effects! I'll keep working on it too, probably. I hope this helps someone 🤝

<iframe style="border-radius:12px" src="https://open.spotify.com/embed/album/6tcl0S3oK680ovj59GurKV?utm_source=generator" width="100%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>

more soon 👏