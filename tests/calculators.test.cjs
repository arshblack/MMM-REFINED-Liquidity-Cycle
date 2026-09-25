const { test } = require('node:test');
const assert = require('node:assert/strict');
const { sizePosition, pipDistance } = require('../assets/calculators.js');
const gold = { riskMoney: '100', entryPrice: '4500', stopPrice: '4490', tickSize: '.01', tickValue: '1', lotStep: '.01', minLot: '.01', maxLot: '100', direction: 'buy' };
test('gold example and forex example with account-currency tick value', () => {
  assert.equal(sizePosition(gold).lots, .1);
  assert.equal(sizePosition(gold).estimatedRisk, 100);
  const fx = sizePosition({ ...gold, entryPrice: '1.25', stopPrice: '1.245', tickSize: '.00001', tickValue: '1' });
  assert.equal(fx.lots, .2);
  assert.ok(Math.abs(fx.estimatedRisk - 100) < 1e-8);
});
test('every numeric field rejects missing, zero, negative and nonfinite values', () => {
  for (const key of Object.keys(gold).filter(k => k !== 'direction')) {
    for (const value of ['', ' ', '0', '-1', 'Infinity', 'NaN', '1e999']) {
      assert.ok(sizePosition({ ...gold, [key]: value }).error, `${key}: ${value}`);
    }
  }
});
test('stop direction and equal prices', () => {
  assert.ok(sizePosition({ ...gold, stopPrice: '4500' }).error);
  assert.ok(sizePosition({ ...gold, stopPrice: '4510' }).error);
  assert.ok(sizePosition({ ...gold, direction: 'sell' }).error);
  assert.equal(sizePosition({ ...gold, direction: 'sell', stopPrice: '4510' }).lots, .1);
});
test('minimum, maximum, fractional steps and downward rounding', () => {
  assert.equal(sizePosition({ ...gold, riskMoney: '5' }).lots, null);
  assert.equal(sizePosition({ ...gold, minLot: '.2' }).lots, null);
  assert.equal(sizePosition({ ...gold, riskMoney: '109' }).lots, .1);
  assert.equal(sizePosition({ ...gold, maxLot: '.05' }).lots, .05);
  assert.equal(sizePosition({ ...gold, riskMoney: '17', lotStep: '.001', minLot: '.001' }).lots, .017);
  assert.ok(sizePosition({ ...gold, minLot: '101' }).error);
});
test('rounded size stays within budget over a range of risks', () => {
  for (let risk = 1; risk < 1000; risk += 7) {
    const result = sizePosition({ ...gold, riskMoney: String(risk), stopPrice: '4486.37' });
    if (result.lots !== null) assert.ok(result.estimatedRisk <= risk + 1e-8);
  }
});
test('pip lab keeps fractional pips and handles flat and invalid inputs', () => {
  assert.equal(pipDistance('4500', '4502', '.01').count, 200);
  assert.equal(pipDistance('4500', '4502', '.1').count, 20);
  assert.ok(Math.abs(pipDistance('4500', '4500.05', '.1').count - .5) < 1e-8);
  assert.equal(pipDistance('4500', '4500', '.01').direction, 'Flat');
  assert.equal(pipDistance('4502', '4500', '.01').direction, 'Down');
  for (const value of ['', '0', '-1', 'Infinity']) assert.ok(pipDistance(value, '4500', '.01').error);
});
