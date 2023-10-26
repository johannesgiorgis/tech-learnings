/**
 * Fluent APIs
 */
class Calculator {
  constructor(private _currentValue: number = 0) {}

  add(a: number): this {
    this._currentValue += a;
    return this;
  }

  subtract(a: number): this {
    this._currentValue -= a;
    return this;
  }

  multiply(a: number): this {
    this._currentValue *= a;
    return this;
  }

  divide(a: number): this {
    this._currentValue /= a;
    return this;
  }

  get value(): number {
    return this._currentValue;
  }
}

let result: number = new Calculator(0)
  .add(5)
  .multiply(2)
  .add(10)
  .divide(4)
  .subtract(2).value;

console.log(`Result: ${result}`);
