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

## Tech

- [Jeff Geerling](https://www.youtube.com/@JeffGeerling)
- [Network Chuck](https://www.youtube.com/@NetworkChuck)

<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Daniel Ramirez's Retro Button</title>
  <style>
    @keyframes pulseShadow {
      0%, 100% {
        box-shadow: 2px 2px 0 #b0b0b0;
      }
      50% {
        box-shadow: 4px 4px 0 #888;
      }
    }
    .webring-button {
      animation: pulseShadow 2s infinite;
      width: 88px;
      height: 31px;
      display: inline-block;
      overflow: hidden;
      cursor: pointer;
      text-decoration: none;
      background: #e0e0e0;
      /* Retro double border: outer dark gray, inner light gray */
      border: 2px solid #b0b0b0;
      box-shadow:
        0 0 0 4px #f8f8f8, /* inner highlight */
        0 0 0 6px #888,     /* outer shadow */
        2px 2px 0 0 #b0b0b0; /* animated shadow */
      margin: 8px;
      padding: 0;
      transition: background 0.1s;
      position: relative;
    }
    .webring-button:hover {
      animation-play-state: paused;
      box-shadow: none;
      background: #d0d0d0;
    }
    .webring-button svg {
      width: 88px;
      height: 31px;
      display: block;
      margin: 0 auto;
    }
  </style>
</head>
<body>
  <a href="https://danialrami.com" class="webring-button" title="danialrami.com!">
    <svg width="88" height="31" viewBox="0 0 264 62" xmlns="http://www.w3.org/2000/svg">
      <!-- Cloud 1 -->
      <g>
        <path d="M44,10 C57,10 66,18 66,29 C79,29 88,37 88,50 C88,62 79,70 66,70 L22,70 C9,70 0,62 0,50 C0,37 9,29 22,29 C22,18 31,10 44,10 Z" fill="#fbf9e2"/>
        <circle cx="31" cy="40" r="7" fill="#000"/>
        <circle cx="57" cy="40" r="7" fill="#000"/>
      </g>
      <!-- Cloud 2 -->
      <g transform="translate(88,0)">
        <path d="M44,10 C57,10 66,18 66,29 C79,29 88,37 88,50 C88,62 79,70 66,70 L22,70 C9,70 0,62 0,50 C0,37 9,29 22,29 C22,18 31,10 44,10 Z" fill="#fbf9e2"/>
        <circle cx="31" cy="40" r="7" fill="#000"/>
        <circle cx="57" cy="40" r="7" fill="#000"/>
      </g>
      <!-- Cloud 3 -->
      <g transform="translate(176,0)">
        <path d="M44,10 C57,10 66,18 66,29 C79,29 88,37 88,50 C88,62 79,70 66,70 L22,70 C9,70 0,62 0,50 C0,37 9,29 22,29 C22,18 31,10 44,10 Z" fill="#fbf9e2"/>
        <circle cx="31" cy="40" r="7" fill="#000"/>
        <circle cx="57" cy="40" r="7" fill="#000"/>
      </g>
    </svg>
  </a>
</body>
</html>
