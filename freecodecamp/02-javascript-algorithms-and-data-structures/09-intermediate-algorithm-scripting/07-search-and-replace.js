/*
You will create a program that takes a sentence, then search for a word in it and replaces it for a new one while preserving the uppercase if there is one.
*/
function myReplace(str, before, after) {
  // handle where before starts with capital letter
  if (before.match(/^[A-Z]/)) {
    console.log('starts with capital');
    after = after.charAt(0).toUpperCase() + after.slice(1);
  }

  var newStr = str.replace(before, after);
  console.log(str, '->', newStr);
  return newStr;
}

// Solution 1
function myReplace1(str, before, after) {
  // Find index where before is on string
  var index = str.indexOf(before);
  // Check to see if the first letter is uppercase or not
  if (str[index] == str[index].toUpperCase()) {
    // Change the after word to be capitalized before we use it
    after = after.charAt(0).toUpperCase() + after.slice(1);
  }
  // Now replace the original str with the edited one.
  str = str.replace(before, after);
  return str;
}

// Solution 2
function myReplace2(str, before, after) {
  // Check if first cahracter of arguments "before" is capital or lowercase letter and change the first character of argument "after" to match the case
  if (/^[A-Z]/.test(before)) {
    after = after[0].toUpperCase() + after.substring(1);
  } else {
    after = after[0].toLowerCase() + after.substring(1);
  }

  // return string with argument "before" replaced by argument "after" (with correct case)
  return str.replace(before, after);
}

// Solution 5 - functional
function myReplace5(str, before, after) {
  const myArr = str.split(' ');
  const [wordToReplace] = myArr.filter(item => item === before);
  return wordToReplace[0].toUpperCase() !== wordToReplace[0]
    ? myArr.map(item => (item === before ? after : item)).join(' ')
    : myArr
      .map(item =>
        item === before ? after[0].toUpperCase() + after.slice(1) : item
      )
      .join(' ');
}

myReplace("A quick brown fox jumped over the lazy dog", "jumped", "leaped");
myReplace("He is Sleeping on the couch", "Sleeping", "sitting");