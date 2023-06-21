function spinalCase(str) {
  // var result = str.toLowerCase().split(' ').join('-'); // initial attempt
  // regex splits on space, underscore and upper case letters
  var regex = / |_|(?=[A-Z])/
  
  var result = str.
    split(regex)        // split into array based on regex
    .join('-')          // join with -
    // .replace(/-+/, '-') // handle case where multiple -
    .toLowerCase();

  console.log(str, '->', result);
  return result;
}

// Solution 1
function spinalCase1(str) {
  // Create a variable for the white space and underscores.
  var regex = /\s+|_+/g;
  console.log(str);

  // Replace low-upper case to low-space-uppercase
  str = str.replace(/([a-z])([A-Z])/g, "$1 $2");
  console.log(str);
  
  // Replace space and underscore with -
  return str.replace(regex, '-').toLowerCase();
}

// Solution 2
function spinalCase2(str) {
  // Replace low-upper case to low-space-uppercase
  str = str.replace(/([a-z])([A-Z])/g, "$1 $2");

  // Split on whitespace and underscores and join with dash
  return str
    .toLowerCase()
    .split(/(?:_| )+/)
    .join('-');
}

// Solution 3 - Potential bug found!
function spinalCase3(str) {
  var result = str
    .split(/\s|_|(?=[A-Z])/)
    .join('-')
    .toLowerCase();
  console.log(str, '->', result);
  return result
}

// spinalCase('This Is Spinal Tap');
spinalCase("this---Is_spinalTap");
