const assert = require('assert');
const calculateNumber = require('./1-calcul.js');

describe('calculateNumber type == SUM', () => {
  it('Integer numbers', () => {
    assert.strictEqual(calculateNumber('SUM', 1, 3), 4);
    assert.strictEqual(calculateNumber('SUM', 3, 6), 9);
    assert.strictEqual(calculateNumber('SUM', 9, 6), 15);
  });
  it('Decimal numbers', () => {
    assert.strictEqual(calculateNumber('SUM', 1.3, 2.6), 4);
    assert.strictEqual(calculateNumber('SUM', 3.0, 4.3), 7);
    assert.strictEqual(calculateNumber('SUM', 8.2, 2.7), 11);
  });
  it('Negative numbers', () => {
    assert.strictEqual(calculateNumber('SUM', -3, 3), 0);
    assert.strictEqual(calculateNumber('SUM', -2.5, 0), -2);
    assert.strictEqual(calculateNumber('SUM', -5.4, 1), -4);
  });
});

describe('calculateNumber type == SUBTRACT', () => {
  it('Integer numbers', () => {
    assert.strictEqual(calculateNumber('SUBTRACT', 3, 1), 2);
    assert.strictEqual(calculateNumber('SUBTRACT', 6, 3), 3);
    assert.strictEqual(calculateNumber('SUBTRACT', 16, 6), 10);
  });
  it('Decimal numbers', () => {
    assert.strictEqual(calculateNumber('SUBTRACT', 4.3, 2.6), 1);
    assert.strictEqual(calculateNumber('SUBTRACT', 7.0, 4.3), 3);
    assert.strictEqual(calculateNumber('SUBTRACT', 9.2, 2.7), 6);
  });
  it('Negative numbers', () => {
    assert.strictEqual(calculateNumber('SUBTRACT', -3, 3), -6);
    assert.strictEqual(calculateNumber('SUBTRACT', -2.5, 1), -3);
    assert.strictEqual(calculateNumber('SUBTRACT', -5.4, 3), -8);
  });
});

describe('calculateNumber type == DIVIDE', () => {
  it('Integer numbers', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 10, 2), 5);
    assert.strictEqual(calculateNumber('DIVIDE', 6, 3), 2);
    assert.strictEqual(calculateNumber('DIVIDE', 16, 4), 4);
  });
  it('Decimal numbers', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 9.3, 2.6), 3);
    assert.strictEqual(calculateNumber('DIVIDE', 8.0, 4.3), 2);
    assert.strictEqual(calculateNumber('DIVIDE', 15.2, 2.7), 5);
  });
  it('Negative numbers', () => {
    assert.strictEqual(calculateNumber('DIVIDE', -9, 3), -3);
    assert.strictEqual(calculateNumber('DIVIDE', -22, 2), -11);
    assert.strictEqual(calculateNumber('DIVIDE', -5.7, 3), -2);
  });
});
