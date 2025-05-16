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
        box-shadow: 4px 4px 0 #555;
      }
      50% {
        box-shadow: 6px 6px 0 #333;
      }
    }

    .webring-button {
      animation: pulseShadow 2s infinite;
      border: 4px double #000;
      padding: 0;
      margin: 8px;
      width: 88px;
      height: 31px;
      background: #e0e0e0;
      cursor: pointer;
      transition: background 0.1s;
      display: inline-block;
      overflow: hidden;
      text-decoration: none;
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
    <svg width="88" height="31" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
      <path d="M100,30 C130,30 150,50 150,80 C180,80 200,100 200,130 C200,160 180,180 150,180 L50,180 C20,180 0,160 0,130 C0,100 20,80 50,80 C50,50 70,30 100,30 Z" fill="#fbf9e2"/>
      <circle cx="70" cy="100" r="15" fill="#000"/>
      <circle cx="130" cy="100" r="15" fill="#000"/>
      <text x="100" y="120" font-family="Verdana, Geneva, sans-serif" font-size="40" fill="#000" text-anchor="middle" alignment-baseline="middle" style="letter-spacing:2px;"></text>
    </svg>
  </a>
</body>
</html>