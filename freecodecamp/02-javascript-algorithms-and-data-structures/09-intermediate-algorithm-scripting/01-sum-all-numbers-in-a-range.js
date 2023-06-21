function sumAll(arr) {
  if (arr[0] < arr[1]) {
    var smallest = arr[0];
    var largest = arr[1];
  } else {
    var smallest = arr[1];
    var largest = arr[0];
  }
  var sum = 0

  for (let i = smallest; i < largest + 1; i++) {
    sum += i;
  }
  console.log(sum);
  return sum;
}

function sumAll1(arr) {
  var max = Math.max(arr[0], arr[1]);
  var min = Math.min(arr[0], arr[1]);
  var sum = 0;
  for (var i = min; i <= max; i++) {
    sum += 1;
  }
  return sum;
}

function sumAll2(arr) {
  // Buckle up everything to one!
  const startNum = arr[0];
  const endNum = arr[1];

  // Get the count of numbers between the two numbers by subtracting them and add 1 to the absolute value.
  // ex. There are |1-4| + 1 = 4, (1, 2, 3, 4), 4 numbers between 1 and 4.
  const numCount = Math.abs(startNum - endNum) + 1;

  // Using Arithmetic Progression summing formula
  const sum = ((startNum + endNum) * numCount) / 2;
  return sum;
}

sumAll([1, 4]);
