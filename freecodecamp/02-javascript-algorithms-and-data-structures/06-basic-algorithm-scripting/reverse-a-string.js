function reverseString(str) {
  // let newArr = [];
  let reversedString = '';
  for (let i = str.length - 1; i >= 0; i--) {
    // console.log(i, str[i]);
    reversedString += str[i];
  }
  // console.log('-----------------')
  return reversedString;
}

reverseString("hello");
