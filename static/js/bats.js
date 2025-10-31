const NUM_BATS = 6;

// === Bat template (inline SVG) ===
const batSVG = `
<svg viewBox="0 0 100 60" aria-hidden="true" focusable="false">
  <path id="leftWing" fill="#111" d="M49,30
    C36,18 26,12 13,14
    C10,9 6,7 2,9
    C6,13 7,18 5,22
    C2,21 1,22 1,24
    C5,27 10,29 15,29
    C17,36 23,42 32,45
    C40,48 45,40 49,30z"/>
  <g id="body" fill="#111">
    <ellipse cx="50" cy="34" rx="5.2" ry="8.8"/>
    <path d="M46.5,26 L48.5,22 L49.8,26 Z"/>
    <path d="M50.2,26 L51.5,22 L53.5,26 Z"/>
  </g>
  <path id="rightWing" fill="#111" d="M51,30
    C64,18 74,12 87,14
    C90,9 94,7 98,9
    C94,13 93,18 95,22
    C98,21 99,22 99,24
    C95,27 90,29 85,29
    C83,36 77,42 68,45
    C60,48 55,40 51,30z"/>
  <circle cx="48.2" cy="32.5" r="0.7" fill="#eee"/>
  <circle cx="51.8" cy="32.5" r="0.7" fill="#eee"/>
</svg>`;

// === Create and animate each bat ===
class Bat {
  constructor(index) {
    this.el = document.createElement('div');
    this.el.className = 'bat';
    this.el.innerHTML = batSVG;
    document.body.appendChild(this.el);

    this.scale = 0.8 + Math.random() * 0.6;
    this.el.style.width = `${80 * this.scale}px`;
    this.el.style.height = `${48 * this.scale}px`;
    this.width = 80 * this.scale;

    this.resetPosition();
    this.flying = false;
    this.animate();
    this.scheduleFlight();
  }

  // Clamp so bats stay within view
  clampX(x) {
    const margin = this.width / 2 + 20;
    return Math.min(window.innerWidth - margin, Math.max(margin, x));
  }

  resetPosition() {
    const rangeFactor = 0.8; 
    this.baseX = this.clampX(Math.random() * window.innerWidth * rangeFactor);
    this.baseY = 10 + Math.random() * 40;
    this.posX = this.baseX;
    this.posY = this.baseY;
    this.targetX = this.baseX;
    this.targetY = this.baseY;
  }

  pickRandomTarget() {
    const margin = this.width / 2 + 20;
    return {
      x: this.clampX(Math.random() * window.innerWidth),
      y: Math.random() * (window.innerHeight / 2) + 40,
    };
  }

  randomFlight() {
    if (this.flying) return;
    this.flying = true;
    this.el.classList.add('flap');
    const t = this.pickRandomTarget();
    this.targetX = t.x;
    this.targetY = t.y;
    setTimeout(() => this.returnHome(), 2000 + Math.random() * 1000);
  }

  returnHome() {
    this.targetX = this.baseX;
    this.targetY = this.baseY;
    setTimeout(() => {
      this.el.classList.remove('flap');
      this.flying = false;
    }, 1800);
  }

  animate() {
    const ease = 0.05;
    this.posX += (this.targetX - this.posX) * ease;
    this.posY += (this.targetY - this.posY) * ease;
    const angle = (this.targetX - this.posX) * 0.05;
    this.el.style.transform = `translate(${this.posX - (this.width / 2)}px, ${this.posY}px) rotate(${angle}deg) scale(${this.scale})`;
    requestAnimationFrame(() => this.animate());
  }

  scheduleFlight() {
    const next = 2000 + Math.random() * 5000;
    setTimeout(() => {
      if (!this.flying) this.randomFlight();
      this.scheduleFlight();
    }, next);
  }
}

// === Create 6 bats ===
for (let i = 0; i < 6; i++) new Bat(i);