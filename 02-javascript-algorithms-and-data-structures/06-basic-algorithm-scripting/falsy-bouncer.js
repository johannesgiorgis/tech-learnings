function bouncer(arr) {
  // Don't show a false ID to this bouncer.
  console.log('input:', arr);
  let newArr = [];
  for (let i = 0; i < arr.length; i++) {
    // let val = arr[i];
    // if (val == false || val === '' || val == 0 || val == undefined || val == NaN) {
    //   arr.splice(i, 1);
    // }
    if (arr[i]) {
      newArr.push(arr[i]);
    }
  }
  console.log(newArr);
  console.log('------');
  return newArr;
}

bouncer([7, "ate", "", false, 9]);
