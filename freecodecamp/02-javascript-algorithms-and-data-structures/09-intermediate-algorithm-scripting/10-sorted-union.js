/*
Write a function that takes two or more arrays and returns a new array of unique values in the order of the original provided arrays.

In other words, all values present from all arrays should be included in their original order, but with no duplicates in the final array.

The unique numbers should be sorted by their original order, but the final array should not be sorted in numerical order.
*/

function uniteUnique(arr) {
  const result = [];
  var args = Array.prototype.slice.call(arguments);
  console.log(args);

  args.forEach((arg) => {
    console.log(arg);
    arg.forEach((num) => {
      if (!result.includes(num)) {
        result.push(num);
      }
    });
  });
  return result;
}

uniteUnique([1, 3, 2], [5, 2, 1, 4], [2, 1]);

// Solution 1
function uniteUnique1(arr1, arr2, arr3) {
  const finalArray = [];

  // Loop through the arguments object to truly make the program work
  // with two or more arrays instead of 3.
  for (let i = 0; i < arguments.length; i++) {
    const arrayArguments = arguments[i];

    // Loops through the array at hand
    for (let j = 0; j < arrayArguments.length; j++) {
      let indexValue = arrayArguments[j];

      // Checks if the value is already on the final array.
      if (finalArray.indexOf(indexValue) < 0) {
        finalArray.push(indexValue);
      }
    }
  }
}

// Solution 2
function uniteUnique2(arr) {
  const args = [...arguments];
  const result = [];
  for (let i = 0; i < args.length; i++) {
    for (let j = 0; j < args[i].length; j++) {
      if (!result.includes(args[i][j])) {
        result.push(args[i][j]);
      }
    }
  }
  return result;
}

// Solution 3
function uniteUnique3(...arr) {
  return [...new Set(arr.flat())];
}

// Solution 4
function uniteUnique4() {
  return [...arguments]
    .flat()
    .filter((item, index, arr) => arr.indexOf(item) === index);
}
