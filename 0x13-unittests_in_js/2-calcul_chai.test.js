const expect = require('chai').expect;
const calculateNumber = require('./2-calcul_chai.js');

describe('calculateNumber type == SUM', () => {
  it('Integer numbers', () => {
    expect(calculateNumber('SUM', 1, 3), 4);
    expect(calculateNumber('SUM', 3, 6), 9);
    expect(calculateNumber('SUM', 9, 6), 15);
  });
  it('Decimal numbers', () => {
    expect(calculateNumber('SUM', 1.3, 2.6), 4);
    expect(calculateNumber('SUM', 3.0, 4.3), 7);
    expect(calculateNumber('SUM', 8.2, 2.7), 11);
  });
  it('Negative numbers', () => {
    expect(calculateNumber('SUM', -3, 3), 0);
    expect(calculateNumber('SUM', -2.5, 0), -2);
    expect(calculateNumber('SUM', -5.4, 1), -4);
  });
});

describe('calculateNumber type == SUBTRACT', () => {
  it('Integer numbers', () => {
    expect(calculateNumber('SUBTRACT', 3, 1), 2);
    expect(calculateNumber('SUBTRACT', 6, 3), 3);
    expect(calculateNumber('SUBTRACT', 16, 6), 10);
  });
  it('Decimal numbers', () => {
    expect(calculateNumber('SUBTRACT', 4.3, 2.6), 1);
    expect(calculateNumber('SUBTRACT', 7.0, 4.3), 3);
    expect(calculateNumber('SUBTRACT', 9.2, 2.7), 6);
  });
  it('Negative numbers', () => {
    expect(calculateNumber('SUBTRACT', -3, 3), -6);
    expect(calculateNumber('SUBTRACT', -2.5, 1), -3);
    expect(calculateNumber('SUBTRACT', -5.4, 3), -8);
  });
});

describe('calculateNumber type == DIVIDE', () => {
  it('Integer numbers', () => {
    expect(calculateNumber('DIVIDE', 10, 2), 5);
    expect(calculateNumber('DIVIDE', 6, 3), 2);
    expect(calculateNumber('DIVIDE', 16, 4), 4);
  });
  it('Decimal numbers', () => {
    expect(calculateNumber('DIVIDE', 9.3, 2.6), 3);
    expect(calculateNumber('DIVIDE', 8.0, 4.3), 2);
    expect(calculateNumber('DIVIDE', 15.2, 2.7), 5);
  });
  it('Negative numbers', () => {
    expect(calculateNumber('DIVIDE', -9, 3), -3);
    expect(calculateNumber('DIVIDE', -22, 2), -11);
    expect(calculateNumber('DIVIDE', -5.7, 3), -2);
  });
  it('Second num is 0', () => {
    expect(calculateNumber('DIVIDE', 3, 0), 'Error');
  });
});
