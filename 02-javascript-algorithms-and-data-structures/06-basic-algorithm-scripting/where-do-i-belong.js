function getIndexToIns(arr, num) {
  // Find my place in this sorted array.
  console.log('input:', arr, num);

  if (arr.length == 0) {
    return 0;
  }

  // sort array in ascending order
  arr.sort(function(a, b){return a-b});
  console.log(arr);

  for (let i = 0; i < arr.length; i++) {
    console.log(i, arr[i], num);
    if (arr[i] > num) {
      console.log(i, arr[i], 'return i:', i);
      console.log('------------------');
      return i;
    } else if (num == arr[i]) {
      console.log(i, arr[i]);
      console.log('------------------');      
      return i;
    }
  }
  console.log(arr.length);
  console.log('------------------');
  return arr.length;
}

getIndexToIns([2, 5, 10], 15);
// getIndexToIns([40, 60], 50);
