var Shape = /** @class */ (function () {
  function Shape(_shapeName) {
    this._shapeName = _shapeName;
    this.displayInformation();
  }
  Object.defineProperty(Shape.prototype, "shapeName", {
    get: function () {
      return this._shapeName;
    },
    enumerable: false,
    configurable: true,
  });
  Shape.prototype.displayInformation = function () {
    console.log("This shape is a ".concat(this._shapeName));
  };
  Shape.prototype.doSomething = function () {
    console.log("Not interesting");
  };
  return Shape;
})();
