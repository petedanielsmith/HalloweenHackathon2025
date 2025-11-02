function revealCard(card) {
    if (document.querySelector('.flip-card.flipped')) {
      document.querySelectorAll('.flip-card:not(.flipped)').forEach(c => c.classList.add('locked'));
      return;
    }

    const outcomes = ["Trick", "Treat"];
    const result = outcomes[Math.floor(Math.random() * outcomes.length)];
    card.classList.add('flipped');
    card.querySelector('.flip-back').innerHTML = result;

    document.querySelectorAll('.flip-card').forEach(c => {
      if (c !== card) c.classList.add('locked');
    });

    if (result.includes("Trick")){
        setTimeout(() => triggerScare(), 1000);
    } else{
        setTimeout(() => showTreat(), 1000);
    }
  }

  function showTreat() {
    const treat = document.getElementById('treatAlert');
    treat.classList.remove('hide-treat');
  }

  function triggerScare() {
    const overlay = document.getElementById('scare-overlay');
    const scream = document.getElementById('scream-sound');
    const laugh = document.getElementById('laugh-sound');

    // Prepare overlay
    overlay.classList.remove('d-none');
    overlay.style.opacity = '0';
    overlay.offsetHeight; // force reflow

    // Flash in quickly
    overlay.classList.add('flicker');
    overlay.style.transition = 'opacity 0.05s ease';
    overlay.style.opacity = '1';

    // Play scream immediately
    scream.currentTime = 0;
    scream.play().catch(()=>{});

    // After a second or so, start fading out and play laugh
    setTimeout(() => {
      laugh.play().catch(()=>{});
      overlay.classList.remove('flicker');
      overlay.style.transition = 'opacity 2s ease';
      overlay.style.opacity = '0';
      setTimeout(() => overlay.classList.add('d-none'), 2000);
    }, 1500);
  }

  // Reset modal state
  const modal = document.getElementById('trickOrTreatModal');
  modal.addEventListener('hidden.bs.modal', () => {
    document.querySelectorAll('.flip-card').forEach(card => {
      card.classList.remove('flipped', 'locked');
      card.querySelector('.flip-back').innerHTML = "";
    });
    const treat = document.getElementById('treatAlert');
    treat.classList.add('hide-treat');
  });