// the global variable
var fixedValue = 4;

// Add your code below this line
function incrementer (counter) {
  counter += 1;
  return counter;

  // Add your code above this line
}

var newValue = incrementer(fixedValue); // Should equal 5
console.log(fixedValue); // Should print 4
