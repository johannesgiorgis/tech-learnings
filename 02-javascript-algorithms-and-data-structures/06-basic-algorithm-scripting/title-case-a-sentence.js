function titleCase(str) {

  let arr = str.toLowerCase().split(' ');
  // console.log('new str:', str);

  // = str.split(' ');

  for (let i = 0; i < arr.length; i++) {
    // console.log(arr[i].toLowerCase());
    // console.log(arr[i], arr[i][0].toUpperCase(), arr[i][0]);
    let str = arr[i];
    let firstChar = arr[i][0];
    // console.log(str.charAt(0), firstChar);
    arr[i] = arr[i].replace(firstChar, firstChar.toUpperCase());
    // str = str.replace(str.charAt(0), str.charAt(0).toUpperCase());    
    // console.log(arr[i], str);
  }
  // console.log(arr.join(' '));
  return arr.join(' ');
}

titleCase("I'm a little tea pot");


// Previous Attempt
// function titleCase(str) {

//   let arr = str.toLowerCase().split(' ');
//   // console.log('new str:', str);

//   // = str.split(' ');

//   for (let i = 0; i < arr.length; i++) {
//     // console.log(arr[i].toLowerCase());
//     // console.log(arr[i], arr[i][0].toUpperCase(), arr[i][0]);
//     let firstChar = arr[i][0];
//     arr[i].replace(firstChar, firstChar.toUpperCase());
//     console.log(arr[i]);
//     // console.log('---------')
//   }
//   console.log(arr.join(' '));
//   return arr.join(' ');
// }

// titleCase("I'm a little tea pot");
