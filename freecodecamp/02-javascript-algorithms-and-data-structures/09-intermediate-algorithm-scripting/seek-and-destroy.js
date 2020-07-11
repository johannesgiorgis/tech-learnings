function destroyer(arr) {
  for (let i = 1; i <= arguments.length; i++) {
    var value = arguments[i];
    arr = arr.filter(num => num != value);
  }
  return arr;
}

// Solution 1
function destroyer1(arr) {
  // convert arguments object to array
  var args = Array.prototype.slice.call(arguments);

  for (var i = 0; i < arr.length; i++) {
    for (var j = 0; j < args.length; j++) {
      if (arr[i] === args[j]) {
        delete arr[i];
      }
    }
  }
  // return array using the Boolean object as a filter for any `null`s created by the `delete` operator
  return arr.filter(Boolean);
}

// Solution 2
function destroyer2(arr) {
  var args = Array.from(arguments).slice(1);
  return arr.filter(function(val) {
    return !args.includes(val);
  });
}

// Solution 3 - ES6 syntax
// Use spreader operator to retrieve the arguments
// Return filtered array using `includes()`
const destroyer3 = (arr, ...valsToRemove) => arr.filter(elem => !valsToRemove.includes(elem));

destroyer([1, 2, 3, 1, 2, 3], 2, 3);
