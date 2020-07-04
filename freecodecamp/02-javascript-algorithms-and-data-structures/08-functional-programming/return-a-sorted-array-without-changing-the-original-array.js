var globalArray = [5, 6, 3, 2, 9];
function nonMutatingSort(arr) {
  // Only change code below this line
  var newArray = [];
  return newArray.concat(arr)
  .sort(function(a, b) {
    return a === b ? 0: a < b ? -1: 1;
  });

  // alternative
  // return [].concat(arr).sort(function(a, b) {
  //   return a - b;
  // });
  // Only change code above this line
}
nonMutatingSort(globalArray);
