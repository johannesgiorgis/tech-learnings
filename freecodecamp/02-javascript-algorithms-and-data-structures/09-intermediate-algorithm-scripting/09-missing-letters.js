/*
Find the missing letter in the passed letter range and return it.

If all letters are present in the range, return undefined.
*/
function fearNotLetter(str) {
  var alphabet = "abcdefghijklmnopqrstuvwxyz";
  console.log(str);
  
  // use indices of first & last characters
  // to extract correct characters from alphabet
  // to compare against passed in string
  var firstChar = str.charAt(0);
  var lastChar = str.charAt(str.length - 1);
  console.log(firstChar, lastChar);
  console.log(alphabet.indexOf(firstChar), 
    alphabet.indexOf(lastChar)
  );
  
  var extracted = alphabet.substr(
    alphabet.indexOf(firstChar), 
    alphabet.indexOf(lastChar) + 1
  );
  console.log('extracted:', extracted);

  for (var c of extracted) {
    // console.log(c, str.indexOf(c));
    if (str.indexOf(c) === -1 ) {
      return c;
    }
  }
  return undefined;
}

// Solution 1
function fearNotLetter1(str) {
  for (var i = 0; i < str.length; i++) {
    /* utf-16 code of current character */
    var code = str.charCodeAt(i);

    /* if code of current character is not equal to first character + no of iteration hence character has been escaped */
    if (code !== str.charCodeAt(0) + i) {
      /* if current character has escaped one character find previous char and return */
      return String.fromCharCode(code - 1);
    }
  }
  return undefined;
}

// Solution 2
function fearNotLetter2(str) {
  // Avoids using 'for' and 'while' loops
  var compare = str.charCodeAt(0), missing;

  str.split('').map(function(letter, index) {
    // compare character codes with the one
    // that should be in that position
    if (str.charCodeAt(index) == compare) {
      ++compare;
    } else {
      missing = String.fromCharCode(compare);
    }
  });

  return missing;
}

// Solution 3
function fearNotLetter3(str) {
  for (let i = 1; i < str.length; ++i) {
    // check if difference in char codes between adjacent characters
    // in the string is more than 1 (check ASCIII table)
    if (str.charCodeAt(i) - str.charCodeAt(i - 1) > 1) {
      return String.fromCharCode(str.charCodeAt(i - 1) + 1);
    }
  }
}

// Solution 4
function fearNotLetter4(str) {
  var allChars = '';
  // select everything except str
  var notChars = new RegExp("[^" + str + "]", "g");

  for (var i = 0; allChars[allChars.length - 1] !== str[str.length - 1]; i++) {
    allChars += String.fromCharCode(str[0].charCodeAt(0) + i);
  }

  // use match() to strip off the str leters from the newly created string and it is returned
  // returned undefined for no missing characters
  return allChars.match(notChars)
    ? allChars.match(notChars).join('')
    : undefined;
}

fearNotLetter("abce");
