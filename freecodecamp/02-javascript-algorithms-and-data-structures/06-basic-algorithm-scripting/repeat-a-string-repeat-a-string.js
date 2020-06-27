function repeatStringNumTimes(str, num) {
  // repeat after me
  if (num < 0) {
    return '';
  } else {
    let newStr = ''
    for (let i = 0; i < num; i++) {
      newStr += str;
    }
    console.log(newStr);
    return newStr;
  }
}

repeatStringNumTimes("abc", 3);
