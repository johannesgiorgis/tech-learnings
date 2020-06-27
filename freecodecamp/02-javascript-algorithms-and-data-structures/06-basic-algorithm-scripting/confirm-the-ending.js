function confirmEnding(str, target) {
  // "Never give up and good luck will find you."
  // -- Falcor
  let index = str.length - target.length;
  console.log(index, str.slice(index));
  let lastPart = str.slice(index);
  return lastPart == target;
}

confirmEnding("Bastian", "n");
