/* Broker inputs are estimates; never substitute a missing field with zero. */
(function (root) {
  'use strict';
  const positive = value => String(value).trim() !== '' && Number.isFinite(Number(value)) && Number(value) > 0;
  function sizePosition(values) {
    const keys = ['riskMoney', 'entryPrice', 'stopPrice', 'tickSize', 'tickValue', 'lotStep', 'minLot', 'maxLot'];
    const invalid = keys.filter(key => !positive(values[key]));
    if (invalid.length) return { error: 'Complete every field with a number greater than zero.', invalid };
    const v = Object.fromEntries(keys.map(key => [key, Number(values[key])]));
    if (v.minLot > v.maxLot || v.lotStep > v.maxLot) return { error: 'Check the broker minimum, maximum and lot step.', invalid: ['minLot', 'maxLot', 'lotStep'] };
    if (!['buy', 'sell'].includes(values.direction)) return { error: 'Choose Buy or Sell.', invalid: ['direction'] };
    if (v.entryPrice === v.stopPrice || (values.direction === 'buy' ? v.stopPrice > v.entryPrice : v.stopPrice < v.entryPrice)) {
      return { error: 'For a buy, the stop must be below entry. For a sell, it must be above entry.', invalid: ['stopPrice'] };
    }
    const distance = Math.abs(v.entryPrice - v.stopPrice);
    const riskPerLot = distance / v.tickSize * v.tickValue;
    if (!Number.isFinite(riskPerLot) || riskPerLot <= 0) return { error: 'These values exceed the calculator range. Check the symbol specification.', invalid: ['tickSize', 'tickValue'] };
    const raw = Math.min(v.riskMoney / riskPerLot, v.maxLot);
    let units = Math.floor(raw / v.lotStep + 1e-10);
    let lots = Number((units * v.lotStep).toPrecision(12));
    // Permit floating-point dust, never a meaningful increase above the risk budget.
    if (lots > v.maxLot + 1e-12 || lots * riskPerLot > v.riskMoney + 1e-8) lots = Number((--units * v.lotStep).toPrecision(12));
    if (!Number.isFinite(lots) || !Number.isSafeInteger(units)) return { error: 'These values exceed the calculator range.', invalid: ['lotStep'] };
    if (lots <= 0 || lots < v.minLot - 1e-12) return { distance, riskPerLot, lots: null, message: 'Below broker minimum. No size fits this risk budget; do not round up.' };
    return { distance, riskPerLot, lots, estimatedRisk: lots * riskPerLot, message: 'Estimate rounded down to the broker lot step. Confirm projected loss in MT5.' };
  }
  function pipDistance(start, end, convention) {
    if (![start, end, convention].every(positive)) return { error: 'Enter positive start and end prices and a pip convention.' };
    const distance = Number(end) - Number(start), count = Math.abs(distance) / Number(convention);
    if (!Number.isFinite(count)) return { error: 'Check the prices and pip convention.' };
    return { distance: Math.abs(distance), count, direction: distance > 0 ? 'Up' : distance < 0 ? 'Down' : 'Flat' };
  }
  if (typeof module !== 'undefined' && module.exports) module.exports = { sizePosition, pipDistance };
  if (!root.document) return;
  const el = id => document.getElementById(id);
  const format = value => value.toLocaleString('en-US', { maximumFractionDigits: 8 });
  if (el('riskMoney')) {
    const ids = ['riskMoney', 'entryPrice', 'stopPrice', 'tickSize', 'tickValue', 'lotStep', 'minLot', 'maxLot', 'direction', 'accountCurrency'];
    const update = () => {
      const values = Object.fromEntries(ids.map(id => [id, el(id).value]));
      const result = sizePosition(values);
      ids.forEach(id => el(id).setAttribute('aria-invalid', String((result.invalid || []).includes(id))));
      const money = n => n.toLocaleString('en-US', { style: 'currency', currency: values.accountCurrency });
      el('stopDistance').textContent = result.error ? '\u2014' : format(result.distance);
      el('riskPerLot').textContent = result.error ? '\u2014' : money(result.riskPerLot);
      el('estimatedLot').textContent = result.error ? '\u2014' : result.lots === null ? 'No size fits' : format(result.lots);
      el('estimatedRisk').textContent = result.error || result.lots === null ? '\u2014' : money(result.estimatedRisk);
      el('riskStatus').textContent = result.error || result.message;
      el('riskStatus').dataset.error = String(!!result.error);
      document.querySelectorAll('[data-account-unit]').forEach(item => { item.textContent = values.accountCurrency; });
    };
    ids.forEach(id => el(id).addEventListener('input', update));
    update();
  }
  if (el('noteStart')) {
    const ids = ['noteStart', 'noteEnd', 'notePip'];
    const update = () => {
      const result = pipDistance(...ids.map(id => el(id).value));
      ids.forEach(id => el(id).setAttribute('aria-invalid', String(!positive(el(id).value))));
      el('noteDistance').textContent = result.error ? '\u2014' : `${format(result.distance)} USD`;
      el('notePipCount').textContent = result.error ? '\u2014' : `${format(result.count)} pips`;
      el('noteDirection').textContent = result.error ? '\u2014' : result.direction;
      el('pipStatus').textContent = result.error || 'The convention changes the pip count, not the price move.';
      el('pipStatus').dataset.error = String(!!result.error);
    };
    ids.forEach(id => el(id).addEventListener('input', update));
    update();
  }
})(typeof globalThis !== 'undefined' ? globalThis : this);
