const squareList = (arr) => {
  // Only change code below this line
  return arr
  .filter(num => num > 0 && num % 1 == 0)
  .map(num => Math.pow(num, 2));
  
  // alternate 1 - using filter & map
  // arr
  //   .filter(num => num > 0 && num % parseInt(num) === 0)
  //   .map(num => Math.pow(num, 2));

  // alternate 2 - using reduce
  // return arr.reduce((sqrIntegers, num) => {
  //   return Number.isInteger(num) && num > 0
  //     ? sqrIntegers.concat(num * num)
  //     : sqrIntegers;
  // }, []);
  // Only change code above this line
};

const squaredIntegers = squareList([-3, 4.8, 5, 3, -3.2]);
console.log(squaredIntegers);
