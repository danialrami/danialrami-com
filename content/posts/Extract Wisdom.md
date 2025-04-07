---
title: Extract Wisdom
date: 2025-04-04
draft: false
---

I'm back from GDC 2025, and was buzzing with ideas, contacts, and insights from the Audio Summit sessions. While in San Francisco, I recorded numerous personal audio notes after talks like Wilbert Roget's talk on the score Helldivers 2 and Cody Matthew Johnson's session on diegetic music in Star Wars Outlaws.

But at least for me, when it comes to audio recordings - they often sit untouched lol. Because reviewing them takes alot of time! So I tried to figure this out with a simple script.

## The Tools, and a chance to soapbox about open source tech

Open source has been a big inspiration for me ever since I graduated university, and I wouldn't know a quarter of the things I know now if amazing open source projects didn't exist. A well maintained open source project with a community behind it is like a public good imo, a problem solved. I stuck two open source projects together with Python and ended up with a tool that can take any audio file as input, transcribe it and sum it up for you with whatever model you like (open source or not). 

OpenAI has a solid tool called Whisper, known for its impressive transcription capabilities - it handles the voice recordings with pretty great accuracy, even in noisy conference environments. It'll take your audio file and turn it into something searchable.

Daniel Miessler's Fabric framework does most of the heavy lifting here, offering community written patterns for "extracting wisdom" from content -- i.e. summarization, but asking for a lot more specifics. [Check out the actual prompt](https://github.com/danielmiessler/fabric/blob/main/patterns/extract_wisdom/system.md) that's running in this script below, which gets fed to whichever model you have set up with fabric. I'm currently switching off between Gemma and Claude, depending on how important this info is to me.

Putting these tools together felt like a no-brainer, but I wanted a seamless workflow that would take me from audio file to insights in one step.

## The Solution

I created a simple Python script that:

1. Takes any audio file as input
2. Transcribes it using Whisper's base model
3. Pipes the transcript through Fabric's extract_wisdom pattern
4. Saves both the transcript and the distillation in a timestamped folder

The extract_wisdom pattern is particularly valuable as it organizes the content into sections like key ideas, deeper insights, notable quotes, and practical recommendations - perfect for something like conference notes from GDC.

## How It Works

The script is straightforward - you run it, point it to your audio file, and it handles the rest. Behind the scenes, it uses Whisper for transcription and then leverages Fabric's pattern through a subprocess call.

What I love about this approach is how it transforms rambling audio notes into structured, actionable insights. A 20-minute recording of my thoughts after the Audio Summit becomes a concise document highlighting the most valuable takeaways.

## Try It Yourself

If you're a sound designer, developer, or anyone who records audio notes, this tool might save you hours of review time. I've made the code available on [GitHub](https://github.com/danialrami/fabric-audio-summary), so feel free to check out the repository and adapt it to your needs. I also wrote an ollama version because open source always wins, but feel free to use your ollama models through fabric too.

Whether you're processing conference recordings, meeting notes, or creative brainstorming sessions, this approach makes your audio content immediately more valuable and accessible.