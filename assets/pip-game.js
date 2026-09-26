(function () {
  'use strict';
  const game = document.getElementById('pip-lab');
  const calculators = window.RLCalculators;
  if (!game || !calculators) return;
  const rounds = [
    { start: '1.2500', end: '1.2525', question: 'GBPUSD moves from 1.2500 to 1.2525. At 0.0001 per pip, how far did price travel?', choices: ['2.5 pips', '25 pips', '250 pips'], answer: () => Math.abs(calculators.pipDistance(1.2500, 1.2525, 0.0001).count - 25) < 1e-7 ? 1 : -1, explain: 'The price difference is 0.0025. Divide by 0.0001 to get 25 pips. It moved up.' },
    { start: '190.00', end: '189.50', question: 'GBPJPY moves from 190.00 to 189.50. At 0.01 per pip, how far did price travel?', choices: ['5 pips down', '50 pips down', '500 pips up'], answer: () => { const result = calculators.pipDistance(190, 189.50, 0.01); return Math.abs(result.count - 50) < 1e-7 && result.direction === 'Down' ? 1 : -1; }, explain: 'The price difference is 0.50. Divide by 0.01 to get 50 pips, and the direction is down.' },
    { start: 'Gold entry 4500', end: 'Stop 4490', question: 'With a $50 loss limit, a 100-ounce gold contract, and 0.01 lot steps, what is the largest estimated size?', choices: ['0.03 lots', '0.05 lots', '0.10 lots'], answer: () => { const result = calculators.sizePosition({ riskMoney: 50, entryPrice: 4500, stopPrice: 4490, tickSize: 0.01, tickValue: 1, lotStep: 0.01, minLot: 0.01, maxLot: 100, direction: 'buy' }); return result.lots === 0.05 ? 1 : -1; }, explain: 'At one lot, a $10 move would lose about $1,000. At 0.05 lot, that is about $50 before costs. Check your broker specifications.' }
  ];
  let index = 0;
  let score = 0;
  const top = game.querySelector('[data-game-top]');
  const track = game.querySelector('[data-game-track]');
  const prices = game.querySelector('[data-game-prices]');
  const question = game.querySelector('[data-game-question]');
  const choices = game.querySelector('[data-game-choices]');
  const feedback = game.querySelector('[data-game-feedback]');
  const next = game.querySelector('[data-game-next]');
  function render() {
    const round = rounds[index];
    top.textContent = `Round ${index + 1} of ${rounds.length}`;
    track.replaceChildren();
    rounds.forEach((_, step) => { const mark = document.createElement('i'); mark.className = step < index ? 'is-done' : step === index ? 'is-current' : ''; track.append(mark); });
    prices.replaceChildren();
    prices.hidden = false;
    [round.start, round.end].forEach((value, step) => { const cell = document.createElement('div'); const label = document.createElement('small'); label.textContent = index === 2 ? (step ? 'Stop' : 'Entry') : (step ? 'Finish' : 'Start'); const number = document.createElement('strong'); number.textContent = value; cell.append(label, number); prices.append(cell); });
    question.textContent = round.question;
    choices.replaceChildren();
    feedback.textContent = '';
    round.choices.forEach((choice, selected) => { const button = document.createElement('button'); button.type = 'button'; button.textContent = choice; button.addEventListener('click', () => answer(selected)); choices.append(button); });
    next.hidden = true;
  }
  function answer(selected) {
    const round = rounds[index];
    const correct = round.answer();
    if (correct < 0) { feedback.textContent = 'This round could not be checked. Try the calculator below.'; return; }
    if (selected === correct) score += 1;
    [...choices.children].forEach((button, choice) => { button.disabled = true; if (choice === correct) button.classList.add('is-correct'); else if (choice === selected) button.classList.add('is-wrong'); });
    feedback.innerHTML = '';
    const verdict = document.createElement('strong'); verdict.textContent = selected === correct ? 'Correct. ' : 'Not quite. ';
    feedback.append(verdict, document.createTextNode(round.explain));
    next.textContent = index === rounds.length - 1 ? 'See result' : 'Next round';
    next.hidden = false;
    next.focus();
  }
  next.addEventListener('click', () => {
    if (index >= rounds.length) { index = 0; score = 0; render(); question.focus(); return; }
    index += 1;
    if (index < rounds.length) { render(); question.focus(); return; }
    top.textContent = 'Practice complete';
    track.replaceChildren(); prices.replaceChildren(); prices.hidden = true; choices.replaceChildren();
    question.textContent = `You got ${score} of ${rounds.length} right.`;
    feedback.textContent = 'Now use your own entry and stop in the calculator below. These are practice examples, not trade signals.';
    next.textContent = 'Play again'; next.hidden = false; next.focus();
  });
  render();
})();
