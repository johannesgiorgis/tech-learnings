function findElement(arr, func) {
  let num = 0;

  for (let i = 0; i < arr.length; i++) {
    let num = arr[i];
    console.log(num, func(num));
    if (func(num) == true) {
      console.log('----------------');
      return num;
    }
  }
  console.log('----------------');
  return undefined;
}

findElement([1, 3, 5, 8, 9, 10], function(num) { return num % 2 === 0; });
// findElement([1, 2, 3, 4], num => num % 2 === 0);
