function frankenSplice(arr1, arr2, n) {
  // It's alive. It's alive!
  console.log('#', arr1, arr2, n);
  let newArr = arr2.slice(0);
  // console.log(newArr, newArr.splice(n, 0, ...arr1));
  newArr.splice(n, 0, ...arr1);
  console.log(newArr);
  console.log('--------------------');
  return newArr;
}

frankenSplice([1, 2, 3], [4, 5, 6], 1);
