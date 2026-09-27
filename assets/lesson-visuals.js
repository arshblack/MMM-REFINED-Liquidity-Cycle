(() => {
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');

  document.querySelectorAll('.lesson-visual[data-frame-base]').forEach((figure) => {
    const image = figure.querySelector('.lesson-visual__image');
    const controls = figure.querySelector('.lesson-visual__controls');
    const count = figure.querySelector('.lesson-visual__count');
    const steps = [...figure.querySelectorAll('.lesson-visual__steps li')];
    const previous = controls.querySelector('[data-action="previous"]');
    const next = controls.querySelector('[data-action="next"]');
    const replay = controls.querySelector('[data-action="replay"]');
    const finalAlt = image.alt;
    let current = 4;
    let timer;

    function stop() {
      window.clearTimeout(timer);
      timer = undefined;
    }

    function show(step) {
      current = Math.max(1, Math.min(4, step));
      image.src = `${figure.dataset.frameBase}${current}.svg`;
      image.alt = current === 4 ? finalAlt : `${figure.dataset.visualTitle}. Step ${current} of 4: ${steps[current - 1].textContent}`;
      count.textContent = `Step ${current} of 4`;
      steps.forEach((item, index) => item.classList.toggle('is-current', index === current - 1));
      previous.disabled = current === 1;
      next.disabled = current === 4;
    }

    function advance() {
      if (current < 4) {
        show(current + 1);
        timer = window.setTimeout(advance, 1700);
      } else {
        stop();
      }
    }

    previous.addEventListener('click', () => { stop(); show(current - 1); });
    next.addEventListener('click', () => { stop(); show(current + 1); });
    replay.addEventListener('click', () => {
      stop();
      show(1);
      if (!reducedMotion.matches) timer = window.setTimeout(advance, 1700);
    });
    reducedMotion.addEventListener('change', () => { if (reducedMotion.matches) stop(); });
    controls.hidden = false;
    show(4);
  });
})();
