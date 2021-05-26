const assert = require('assert');
const calculateNumber = require('./0-calcul.js');

describe('calculateNumber', () => {
  it('Integer numbers', () => {
    assert.strictEqual(calculateNumber(1, 3), 4);
    assert.strictEqual(calculateNumber(3, 6), 9);
    assert.strictEqual(calculateNumber(9, 6), 15);
  });
  it('Decimal numbers', () => {
    assert.strictEqual(calculateNumber(1.3, 2.6), 4);
    assert.strictEqual(calculateNumber(3.0, 4.3), 7);
    assert.strictEqual(calculateNumber(8.2, 2.7), 11);
  });
  it('Negative numbers', () => {
    assert.strictEqual(calculateNumber(-3, 3), 0);
    assert.strictEqual(calculateNumber(-2.5, 0), -2);
    assert.strictEqual(calculateNumber(-5.4, 1), -4);
  });
  it('NaN', () => {
    assert.strictEqual(isNaN(calculateNumber(3.7)), true);
    assert.strictEqual(isNaN(calculateNumber()), true);
    assert.strictEqual(isNaN(calculateNumber("d")), true);
  });
});
