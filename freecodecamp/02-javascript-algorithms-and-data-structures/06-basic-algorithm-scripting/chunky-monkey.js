function chunkArrayInGroups(arr, size) {
  // Break it up.
  console.log('input:', arr, size);

  let newArr = []
  if (arr.length % size == 0) {
    for (let i = 0; i < arr.length; i += size) {
      console.log(i, size,  arr.slice(i, i+size));
      newArr.push(arr.slice(i, i+size));
    }
  } else {
    for (let i = 0; i < arr.length; i += size) {
      console.log(i, size,  arr.slice(i, i+size));
      newArr.push(arr.slice(i, i+size));
    }
  }

  console.log(newArr);
  console.log('-------------------');
  return newArr;
}

chunkArrayInGroups(["a", "b", "c", "d"], 2);
