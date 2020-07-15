/*
You need to create a program that will translate from English to Pig Latin. Pig Latin takes the first consonant (or consonant cluster) of an English word, moves it to the end of the word and suffixes an “ay”. If a word begins with a vowel you just add “way” to the end. It might not be obvious but you need to remove all the consonants up to the first vowel in case the word does not start with a vowel.
*/

function translatePigLatin(str) {
  var vowels_regex = /(a|e|u|i|o)/
  console.log(str);

  if (str.match(/^(a|e|u|i|o)/)) {
    console.log('starts with a vowel!');
    str += 'way';
  } else {
    console.log('starts with a consonant!');
    var strArray = str.split(vowels_regex);
    console.log('\t', strArray);
    console.log('\t', strArray.slice(1,))
    str = strArray.slice(1).join('') + strArray[0]
    str += 'ay'
  }
  console.log('->', str)
  return str;
}

/* Solution 1
- start at beginning & get longest match of everything not a vowel
- if regex pattern found, it saves the match; else it returns null
- if regex pattern found (starts with consonants), it deletes match
*/
function translatePigLatin1(str) {
  let consonantRegex = /^[^aeiou]+/;
  let myConsonants = str.match(consonantRegex);
  return myConsonants !== null
    ? str
      .replace(consonantRegex, '')
      .concat(myConsonants)
      .concat('ay')
    : str.concat('way');
}

// Solution 2
function translatePigLatin2(str) {
  var pigLatin = '';
  var regex = /[aeiou]/gi;

  // Check if the first character is a vowel
  if (str[0].match(regex)) {
    pigLatin = str + 'way';
  } else if (str.match(regex) === null) {
    // Check if the string contains only consonants
    pigLatin = str + 'ay';
  } else {
    // Find how many consonants before the first vowel.
    var vowelIndice = str.indexOf(str.match(regex)[0]);

    // Take the string from the first vowel to the last char
    // then add the consonants that were previously omitted and add the ending.
    pigLatin = str.substr(vowelIndice) + str.substr(0, vowelIndice) + 'ay';
  }

  return pigLatin;
}

// Solution 3
function translatePigLatin3(str) {
  if (str.match(/^[aeiou]/)) return str + 'way';

  // build a string which contains every consonant before the first vowel in the provided string
  const consonantCluster = str.match(/^[^aeiou]+/)[0];
  return str.substring(consonantCluster.length) + consonantCluster + 'ay';
}

/* Solution 4
- Use `replace()` on string using a regex to check if the first letter is a vowel and adding way at the end of this case
- Use `replace()` again to check for consonants at the beginning of the word and to move it or them to the end of the word and add ay at the end
*/
function translatePigLatin4(str) {
  return str
    .replace(/^[aeiou]\w*/, "$&way")
    .replace(/(^[^aeiou]+)(\w*)/, "$2$1ay");
}

/* Solution 5 - Recursive Solution */
function translatePigLatin5(str, charPos = 0) {
  return ['a', 'e', 'i', 'o', 'u'].includes(str[0])
    ? str + (charPos === 0 ? 'way': 'ay')
    : charPos === str.length
      ? str + 'ay'
      : translatePigLatin5(str.slice(1) + str[0], charPos + 1);
}

translatePigLatin("consonant");
translatePigLatin("schwartz");
translatePigLatin("rhythm");
