(() => {
  const progress = document.querySelector('.read-progress');
  const updateProgress = () => {
    if (!progress) return;
    const total = document.documentElement.scrollHeight - innerHeight;
    progress.style.width = `${total > 0 ? Math.min(100, scrollY / total * 100) : 0}%`;
  };
  addEventListener('scroll', updateProgress, { passive: true });
  updateProgress();

  document.querySelectorAll('[data-quote-shift]').forEach(button => {
    button.addEventListener('click', () => {
      const shift = Number(button.dataset.quoteShift);
      const price = document.querySelector('[data-quote-price]');
      const result = document.querySelector('[data-quote-result]');
      if (!price || !result) return;
      document.querySelectorAll('[data-quote-shift]').forEach(item => item.setAttribute('aria-pressed', String(item === button)));
      price.textContent = (4500 + shift).toFixed(2);
      result.textContent = shift > 0
        ? 'The quote rose: gold became more expensive in US-dollar terms. That does not reveal which participant caused the move.'
        : shift < 0
          ? 'The quote fell: gold became cheaper in US-dollar terms. Direction alone does not explain the cause.'
          : 'The quote is unchanged. XAUUSD simply expresses gold in US-dollar terms.';
    });
  });

  const driverInputs = [...document.querySelectorAll('[data-driver]')];
  const updateDrivers = () => {
    if (!driverInputs.length) return;
    const values = Object.fromEntries(driverInputs.map(input => [input.dataset.driver, input.value]));
    const lines = [];
    if (values.dollar === 'weaker') lines.push('a weaker dollar can support gold in dollar terms');
    if (values.dollar === 'stronger') lines.push('a stronger dollar can pressure gold in dollar terms');
    if (values.rates === 'falling') lines.push('falling real yields can reduce gold’s opportunity cost');
    if (values.rates === 'rising') lines.push('rising real yields can increase gold’s opportunity cost');
    if (values.risk === 'high') lines.push('risk demand can increase safe-haven interest');
    if (values.risk === 'low') lines.push('quiet risk conditions can reduce that source of demand');
    const scores = {
      weaker: 1, stronger: -1, falling: 1, rising: -1, high: 1, low: -1, neutral: 0
    };
    const score = driverInputs.reduce((total, input) => total + scores[input.value], 0);
    const active = driverInputs.filter(input => input.value !== 'neutral').length;
    document.querySelector('[data-driver-title]').textContent = active === 0
      ? 'No directional pressure selected'
      : score >= 2
        ? 'Historically supportive context, still not a signal'
        : score <= -2
          ? 'Historically restrictive context, still not a signal'
          : 'Mixed pressure, confirmation required';
    document.querySelector('[data-driver-copy]').textContent = lines.length
      ? `${lines.join('; ')}. These are historical relationships, not a forecast for the next candle.`
      : 'The selected inputs are neutral. Price structure and actual market response still matter.';
  };
  driverInputs.forEach(input => input.addEventListener('change', updateDrivers));
  updateDrivers();

  const filters = [...document.querySelectorAll('[data-note-filter]')];
  const rows = [...document.querySelectorAll('[data-note-topic]')];
  filters.forEach(button => button.addEventListener('click', () => {
    const topic = button.dataset.noteFilter;
    filters.forEach(item => item.setAttribute('aria-pressed', String(item === button)));
    rows.forEach(row => { row.hidden = topic !== 'all' && row.dataset.noteTopic !== topic; });
  }));
})();
