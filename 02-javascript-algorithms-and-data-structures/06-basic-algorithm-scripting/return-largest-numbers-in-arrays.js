function largestOfFour(arr) {
  // You can do this!
  let newArr = [];

  for (let i = 0; i < arr.length; i++) {
    let maxNum = arr[i][0];
    console.log(arr[i])
    for (let j = 0; j < arr[i].length; j++) {
      console.log(arr[i][j]);
      if (maxNum < arr[i][j]) {
        console.log('\tupdating maxNum to', arr[i][j])
        maxNum = arr[i][j];
      }
    }
    newArr.push(maxNum);
    console.log('max:', maxNum);
    // console.log(arr[i])
  }
  return newArr;
}

largestOfFour([[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]]);
