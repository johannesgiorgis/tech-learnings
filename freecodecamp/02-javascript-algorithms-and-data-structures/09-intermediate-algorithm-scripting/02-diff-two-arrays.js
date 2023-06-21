function diffArray(arr1, arr2) {
  var newArr = [];
  console.log(arr1.length);

  // iterate through arr1 items
  for (let i = 0; i < arr1.length; i++) {
    if (arr2.indexOf(arr1[i]) == -1) {
      newArr.push(arr1[i]);
    }
  }

  // iterate through arr2 items
  for (let j = 0; j < arr2.length; j++) {
    if (arr1.indexOf(arr2[j]) == -1) {
      newArr.push(arr2[j]);
    }
  }

  console.log(newArr);
  return newArr;
}

// Imperative solution
function diffArray1(arr1, arr2) {
  var newArr = [];

  function onlyInFirst(first, second) {
    // Looping through an array to find elements that don't exist in another array
    for (var i = 0; i < first.length; i++) {
      if (second.indexOf(first[i]) === -1) {
        // Pushing the elements unique to first to newArr
        newArr.push(first[i]);
      }
    }
  }

  onlyInFirst(arr1, arr2);
  onlyInFirst(arr2, arr1);

  return newArr;
}

// Declarative solution
function diffArray2(arr1, arr2) {
  return arr1
    .concat(arr2)
    .filter(item => !arr1.includes(item) || !arr2.includes(item));
}

// Declarative Solution 2
function diffArray3(arr1, arr2) {
  return [...diff(arr1, arr2), ...diff(arr2, arr1)];

  function diff(a, b) {
    return a.filter(item => b.indexOf(item) === -1);
  }
}

diffArray([1, 2, 3, 5], [1, 2, 3, 4, 5]);
