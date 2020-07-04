// The global variable
var globalTitle = "Winter Is Coming";

// Only change code below this line
function urlSlug(title) {
  var newTitle = title.
  toLowerCase().
  split(' ').
  filter(obj => {
    return obj != '';
  }).join('-');
  console.log(newTitle);
  return newTitle;

  // alternative
  // return title
  //   .toLowerCase()
  //   .trim()
  //   .split(/\s+/)
  //   .join('-');
}
// Only change code above this line
