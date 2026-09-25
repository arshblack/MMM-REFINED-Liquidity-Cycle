(function (root) {
  'use strict';
  const presets = {
    XAUUSD: { base: 'XAU', quote: 'USD', contract: 100, tick: .01, pip: null, entry: 4500, stop: 4490 },
    EURUSD: { base: 'EUR', quote: 'USD', contract: 100000, tick: .00001, pip: .0001, entry: 1.1, stop: 1.095 },
    GBPUSD: { base: 'GBP', quote: 'USD', contract: 100000, tick: .00001, pip: .0001, entry: 1.3, stop: 1.295 },
    USDJPY: { base: 'USD', quote: 'JPY', contract: 100000, tick: .001, pip: .01, entry: 150, stop: 149.5 },
    USDCHF: { base: 'USD', quote: 'CHF', contract: 100000, tick: .00001, pip: .0001, entry: .9, stop: .895 },
    USDCAD: { base: 'USD', quote: 'CAD', contract: 100000, tick: .00001, pip: .0001, entry: 1.35, stop: 1.345 },
    AUDUSD: { base: 'AUD', quote: 'USD', contract: 100000, tick: .00001, pip: .0001, entry: .65, stop: .645 },
    NZDUSD: { base: 'NZD', quote: 'USD', contract: 100000, tick: .00001, pip: .0001, entry: .6, stop: .595 },
    GBPJPY: { base: 'GBP', quote: 'JPY', contract: 100000, tick: .001, pip: .01, entry: 190, stop: 189.5 },
    EURGBP: { base: 'EUR', quote: 'GBP', contract: 100000, tick: .00001, pip: .0001, entry: .85, stop: .845 },
    GBPNZD: { base: 'GBP', quote: 'NZD', contract: 100000, tick: .00001, pip: .0001, entry: 2.3, stop: 2.295 }
  };
  const positive = v => String(v).trim() !== '' && Number.isFinite(Number(v)) && Number(v) > 0;
  function preparePlan(values, referenceRate) {
    const preset = presets[values.instrument];
    if (!preset) return { error: 'Choose an instrument.', invalid: ['instrument'] };
    const invalid = ['accountSize', 'riskPercent', 'entryPrice', 'stopPrice'].filter(key => !positive(values[key]));
    if (invalid.length) return { error: 'Enter your account size, risk percentage, entry and stop.', invalid };
    if (Number(values.riskPercent) > 100) return { error: 'Risk percentage cannot exceed 100.', invalid: ['riskPercent'] };
    let tickSize = preset.tick, tickValue;
    const rate = values.accountCurrency === preset.quote ? 1 : values.accountCurrency === preset.base ? 1 / Number(values.stopPrice) : referenceRate;
    if (values.brokerOverride) {
      tickSize = values.tickSize; tickValue = values.tickValue;
    } else {
      if (!positive(rate)) return { error: 'Conversion unavailable. Use your broker tick value in Broker details, or retry the rate.', invalid: [] };
      tickValue = preset.contract * preset.tick * Number(rate);
    }
    const riskMoney = Number(values.accountSize) * Number(values.riskPercent) / 100;
    if (!Number.isFinite(riskMoney) || riskMoney <= 0) return { error: 'Check account size and risk percentage.', invalid: ['accountSize', 'riskPercent'] };
    return { ...values, riskMoney, tickSize, tickValue, preset, rate };
  }
  if (typeof module !== 'undefined' && module.exports) module.exports = { presets, preparePlan };
  if (!root.document || !document.getElementById('instrument')) return;
  const el = id => document.getElementById(id);
  const ids = ['instrument','accountCurrency','accountSize','riskPercent','entryPrice','stopPrice','direction','tickSize','tickValue','lotStep','minLot','maxLot'];
  let referenceRate = null, rateNote = '', request;
  const fmt = n => n.toLocaleString('en-US', { maximumFractionDigits: 6 });
  function read() { return { ...Object.fromEntries(ids.map(id => [id, el(id).value])), brokerOverride: el('brokerOverride').checked }; }
  function update() {
    const values = read(), preset = presets[values.instrument];
    const plan = preparePlan(values, referenceRate);
    const result = plan.error ? plan : root.RLCalculators.sizePosition(plan);
    const money = n => n.toLocaleString('en-US', { style: 'currency', currency: values.accountCurrency });
    ids.forEach(id => el(id).setAttribute('aria-invalid', String((result.invalid || []).includes(id))));
    el('estimatedLot').textContent = result.error ? '\u2014' : result.lots === null ? 'No size fits' : fmt(result.lots);
    el('estimatedRisk').textContent = result.error || result.lots === null ? '\u2014' : money(result.estimatedRisk);
    el('riskBudget').textContent = plan.error ? '\u2014' : money(plan.riskMoney);
    el('stopDistance').textContent = result.error ? '\u2014' : preset.pip ? `${fmt(result.distance / preset.pip)} pips` : `${fmt(result.distance)} USD / oz`;
    el('riskStatus').textContent = result.error || (result.lots === null ? result.message : `Estimated ${values.instrument} size: ${fmt(result.lots)} lots. If the stop fills at your price, the estimated loss is ${money(result.estimatedRisk)} before costs.`);
    el('riskStatus').dataset.error = String(!!result.error);
    el('assumptions').textContent = values.brokerOverride ? 'Using your broker tick size and loss tick value. Verify that both belong to this symbol and account currency.' : `Standard-contract estimate: ${fmt(preset.contract)} ${preset.base === 'XAU' ? 'troy ounces' : preset.base + ' units'} per lot. ${preset.pip ? '1 pip = ' + preset.pip + ' in price.' : 'Gold is shown as price distance, because pip conventions vary.'} Broker volume limits below are editable assumptions.`;
    const direct = values.accountCurrency === preset.quote;
    const inverse = values.accountCurrency === preset.base;
    el('conversionNote').textContent = values.brokerOverride ? 'Broker value supplied in ' + values.accountCurrency + '.' : direct ? `Quote and account are both ${preset.quote}; no conversion needed.` : inverse ? `Converting ${preset.quote} to ${values.accountCurrency} at your stop price.` : rateNote;
    el('retryRate').hidden = values.brokerOverride || direct || inverse || referenceRate !== null;
    el('tickSize').disabled = el('tickValue').disabled = !values.brokerOverride;
    document.querySelectorAll('[data-account-unit]').forEach(item => { item.textContent = values.accountCurrency; });
  }
  async function refreshRate() {
    request?.abort();
    request = new AbortController();
    const current = request, values = read(), preset = presets[values.instrument];
    referenceRate = null;
    rateNote = 'Loading a daily reference conversion rate...';
    update();
    if (values.brokerOverride || [preset.base, preset.quote].includes(values.accountCurrency)) return;
    const timeout = setTimeout(() => current.abort(), 8000);
    try {
      const response = await fetch(`https://api.frankfurter.dev/v2/rate/${preset.quote}/${values.accountCurrency}`, { signal: current.signal, credentials: 'omit', referrerPolicy: 'no-referrer' });
      if (!response.ok) throw new Error('rate unavailable');
      const data = await response.json();
      const age = Date.now() - Date.parse(data.date + 'T00:00:00Z');
      if (!positive(data.rate) || data.base !== preset.quote || data.quote !== values.accountCurrency || !Number.isFinite(age) || age < -86400000 || age > 7 * 86400000) throw new Error('rate invalid or stale');
      if (request !== current) return;
      referenceRate = Number(data.rate);
      rateNote = `Daily reference: 1 ${preset.quote} = ${fmt(referenceRate)} ${values.accountCurrency} (${data.date}, Frankfurter). Not a live broker conversion.`;
    } catch (_) {
      if (request !== current) return;
      rateNote = 'Daily conversion is unavailable or out of date. Enter your broker loss tick value below.';
    } finally { clearTimeout(timeout); if (request === current) update(); }
  }
  ids.forEach(id => el(id).addEventListener('input', () => {
    if (id === 'instrument') {
      el('entryPrice').value = el('stopPrice').value = '';
      el('brokerOverride').checked = false;
      el('tickSize').value = presets[el('instrument').value].tick;
      el('tickValue').value = '';
      el('lotStep').value = el('minLot').value = '.01'; el('maxLot').value = '100';
      refreshRate();
    } else if (id === 'accountCurrency') {
      el('brokerOverride').checked = false; el('tickValue').value = ''; refreshRate();
    } else update();
  }));
  el('brokerOverride').addEventListener('change', refreshRate);
  el('retryRate').addEventListener('click', refreshRate);
  el('loadExample').addEventListener('click', () => {
    const preset = presets[el('instrument').value];
    el('entryPrice').value = preset.entry; el('stopPrice').value = preset.stop; el('direction').value = 'buy'; update();
  });
  refreshRate();
})(typeof globalThis !== 'undefined' ? globalThis : this);
