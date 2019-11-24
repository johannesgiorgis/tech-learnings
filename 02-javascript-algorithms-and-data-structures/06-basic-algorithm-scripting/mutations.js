function mutation(arr) {

  console.log('input:', arr);

  // lowercase everything
  for (let i = 0; i < arr.length; i++) {
    arr[i] = arr[i].toLowerCase();
    console.log(arr[i]);
  }
  console.log(arr);

  let firstStr = arr[0];
  let secondStr = arr[1];

  for (let j = 0; j < secondStr.length; j++) {
    console.log(firstStr.indexOf(secondStr[j]));
    if (firstStr.indexOf(secondStr[j]) == -1) {
      return false
    }
  }
  console.log('---------------------');
  return true;
}

mutation(["hello", "hey"]);
