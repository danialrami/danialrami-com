---
title: People
date: 2025-01-01
draft: false
---

I'll link to other people's websites here. I'm taking inspiration from [webrings](https://indieweb.org/webring) on this page.

## Music
- [Music Thing Modular](https://www.musicthing.co.uk/)
- [Perfect Circuit](https://www.perfectcircuit.com/signal)
- [Airwiggles](https://www.airwiggles.com/)
- [Justin Tomchuk](https://justintomchuk.com/)
- [Rodrigo Constanzo](https://rodrigoconstanzo.com/)
- [Rob Bridgett](https://robbridgett.com/)
- [nadia.audio](https://nadia.audio/)
- [Michael Britten](https://michaelbritten.music/)

## [Indieweb](https://indieweb.org/) Stuff
- [32bit.cafe](https://32bit.cafe/)
- [Dreamwidth](https://www.dreamwidth.org/)
- [Hotline](https://hotlinewebring.club/)
- [foreverliketh.is](https://foreverliketh.is/)
- [wiby](https://wiby.org/)
- [micro.blog](https://micro.blog/)
- [skyjake](https://gmi.skyjake.fi/)

## Tech

- [Jeff Geerling](https://www.youtube.com/@JeffGeerling)
- [Network Chuck](https://www.youtube.com/@NetworkChuck)


<html lang="en">

<head>

<meta charset="UTF-8">

<title>Daniel Ramirez's Retro Button</title>

<style>

/* Base button styles with exact dimensions */

.dr-button {

width: 88px;

height: 31px;

display: inline-block;

position: relative;

overflow: hidden;

cursor: pointer;

text-decoration: none;

}

/* Button background */

.button-bg {

position: absolute;

top: 0;

left: 0;

width: 100%;

height: 100%;

background-color: rgba(50, 50, 50, 0.2);

z-index: 1;

}

/* Button SVG container */

.button-content {

position: relative;

z-index: 2;

width: 100%;

height: 100%;

}

/* Cloud animation */

@keyframes float {

0%, 100% { transform: translateY(0); }

50% { transform: translateY(-2px); }

}

/* Eye blink animation */

@keyframes eyeBlink {

0%, 95%, 100% { transform: scaleY(1); }

97% { transform: scaleY(0.1); }

}

/* Sparkle animation */

@keyframes sparkle {

0%, 100% { opacity: 0; transform: scale(0.5); }

50% { opacity: 1; transform: scale(1); }

}

.sparkle {

position: absolute;

width: 3px;

height: 3px;

background: rgba(255, 255, 255, 0.7);

border-radius: 50%;

z-index: 3;

animation: sparkle 3s infinite;

}

</style>

</head>

<body>

<a href="https://danialrami.com" class="dr-button" title="danialrami.com">

<div class="button-bg"></div>

<div class="button-content">

<svg width="88" height="31" viewBox="0 0 88 31" xmlns="http://www.w3.org/2000/svg">

<style>

.cloud { animation: float 3s ease-in-out infinite; }

.cloud:nth-child(1) { animation-delay: 0s; }

.cloud:nth-child(2) { animation-delay: 0.7s; }

.cloud:nth-child(3) { animation-delay: 1.3s; }

.eye { animation: eyeBlink 4s infinite; transform-origin: center; }

.cloud:nth-child(1) .eye { animation-delay: 0s; }

.cloud:nth-child(2) .eye { animation-delay: 1.5s; }

.cloud:nth-child(3) .eye { animation-delay: 2.7s; }

</style>

<!-- First Cloud -->

<g class="cloud">

<path d="M15,5 C19,5 22,7 22,11 C26,11 29,14 29,18 C29,22 26,25 22,25 L8,25 C4,25 1,22 1,18 C1,14 4,11 8,11 C8,7 11,5 15,5 Z"

fill="#d8d8d8" stroke="#888" stroke-width="1"/>

<circle class="eye" cx="11" cy="16" r="2" fill="#222"/>

<circle class="eye" cx="19" cy="16" r="2" fill="#222"/>

</g>

<!-- Second Cloud -->

<g class="cloud">

<path d="M44,5 C48,5 51,7 51,11 C55,11 58,14 58,18 C58,22 55,25 51,25 L37,25 C33,25 30,22 30,18 C30,14 33,11 37,11 C37,7 40,5 44,5 Z"

fill="#d8d8d8" stroke="#888" stroke-width="1"/>

<circle class="eye" cx="40" cy="16" r="2" fill="#222"/>

<circle class="eye" cx="48" cy="16" r="2" fill="#222"/>

</g>

<!-- Third Cloud -->

<g class="cloud">

<path d="M73,5 C77,5 80,7 80,11 C84,11 87,14 87,18 C87,22 84,25 80,25 L66,25 C62,25 59,22 59,18 C59,14 62,11 66,11 C66,7 69,5 73,5 Z"

fill="#d8d8d8" stroke="#888" stroke-width="1"/>

<circle class="eye" cx="69" cy="16" r="2" fill="#222"/>

<circle class="eye" cx="77" cy="16" r="2" fill="#222"/>

</g>

</svg>

</div>

<!-- Add sparkles with script -->

<script>

(function() {

// Create sparkles immediately

const createSparkles = function() {

const button = document.querySelector('.dr-button');

if (!button) return;

// Create 10 sparkles

for (let i = 0; i < 10; i++) {

const sparkle = document.createElement('div');

sparkle.className = 'sparkle';

// Random position

sparkle.style.left = Math.floor(Math.random() * 88) + 'px';

sparkle.style.top = Math.floor(Math.random() * 31) + 'px';

// Random delay

sparkle.style.animationDelay = (Math.random() * 3) + 's';

button.appendChild(sparkle);

}

};

// Run immediately or when DOM is ready

if (document.readyState === 'loading') {

document.addEventListener('DOMContentLoaded', createSparkles);

} else {

createSparkles();

}

})();

</script>

</a>

</body>

</html>