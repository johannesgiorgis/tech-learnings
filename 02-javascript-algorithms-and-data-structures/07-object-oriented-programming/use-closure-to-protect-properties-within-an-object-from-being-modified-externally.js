function Bird() {
  let weight = 15; // private variable

  /* publicly available method that a bird object can use */
  this.getWeight = function() {
    return weight;
  };
}

let bird = new Bird();
bird.getWeight();