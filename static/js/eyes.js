function spawnEvilEyes() {
    const eyes = document.createElement('div');
    eyes.className = 'evil-eye';

    // Inline SVG of sharp glowing eyes
    eyes.innerHTML = `
    <svg viewBox="0 0 100 60" width="100" height="60">
      <defs>
        <filter id="glow">
          <feGaussianBlur stdDeviation="2.5" result="blur"/>
          <feMerge>
            <feMergeNode in="blur"/>
            <feMergeNode in="SourceGraphic"/>
          </feMerge>
        </filter>
      </defs>

      <!-- Left eye -->
      <path d="M15,30 Q28,15 40,30 Q28,45 15,30 Z"
            fill="red" stroke="darkred" stroke-width="1.5"
            filter="url(#glow)" />
      <!-- Right eye -->
      <path d="M60,30 Q72,15 85,30 Q72,45 60,30 Z"
            fill="red" stroke="darkred" stroke-width="1.5"
            filter="url(#glow)" />
    </svg>
    `;

    // Random position
    const x = Math.random() * (window.innerWidth - 100);
    const y = Math.random() * (window.innerHeight * 0.6) + 50;
    eyes.style.left = `${x}px`;
    eyes.style.top = `${y}px`;

    // Random scaling & hue
    const scale = 0.2 + Math.random() * 1.2;
    const hue = Math.random() * 20; // red/yellow tint
    eyes.style.transform = `scale(${scale})`;
    eyes.querySelectorAll('path').forEach(p => {
      p.setAttribute('fill', `hsl(${hue}, 100%, 50%)`);
      p.setAttribute('stroke', `hsl(${hue}, 80%, 25%)`);
    });

    document.body.appendChild(eyes);

    // Fade in
    requestAnimationFrame(() => eyes.style.opacity = 1);

    // Start flicker
    eyes.classList.add('flicker');

    // Fade out and remove
    const lifespan = 3000 + Math.random() * 3000;
    setTimeout(() => {
      eyes.style.opacity = 0;
      eyes.classList.remove('flicker');
      setTimeout(() => eyes.remove(), 1000);
    }, lifespan);
  }

  // Spawn new sets of eyes occasionally
  setInterval(() => {
    if (Math.random() < 0.6) spawnEvilEyes();
  }, 1500);