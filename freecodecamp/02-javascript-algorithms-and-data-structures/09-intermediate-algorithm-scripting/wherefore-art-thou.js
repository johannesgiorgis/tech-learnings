function whatIsInAName(collection, source) {
  var arr = [];
  // Only change code below this line
  var srcKeys = Object.keys(source);

  for (var i = 0; i < collection.length; i++) {
    var item = collection[i];
    console.log('item:', item,'| source:', source, '| keys:', srcKeys);
    
    var to_add = true
    for (let key in source) {
      console.log('\t', key, '->', source[key], '|item:', item[key]);
      if (!item.hasOwnProperty(key) || item[key] !== source[key]) {
        to_add = false   
      };
    }

    // add if found all matching properties with keys/values
    console.log('\tto_add:', to_add);
    if (to_add === true) {
      arr.push(item);
    }
  
  }
  console.log();

  // Only change code above this line
  return arr;
}

// Solution 1 - use Array.prototype.filter method
function whatIsInAName1(collection, source) {
  var srcKeys = Object.keys(source);

  // filter the collection
  return collection.filter(function(obj) {
    for (var i = 0; i < srcKeys.length; i++) {
      if (
        !obj.hasOwnProperty(srcKeys[i]) ||
        obj[srcKeys[i]] !== source[srcKeys[i]]
      ) {
        return false;
      }
    }
    return true;
  });
}

// Solution 1 - my variation - no need for indexes/lengths
function whatIsInAName12(collection, source) {
  var srcKeys = Object.keys(source);

  // filter the collection
  return collection.filter(function(obj) {
    for (var key in srcKeys) {
      if (
        !obj.hasOwnProperty(key) || obj[key] !== source[key]
      ) {
        return false;
      }
    }
    return true;
  });
}

// Solution 2
function whatIsInAName2(collection, source) {
  var srcKeys = Object.keys(source);

  return collection.filter(function(obj) {
    return srcKeys.every(function(key) {
      return obj.hasOwnProperty(key) && obj[key] === source[key];
    });
  });
}

// Solution 3
function whatIsInAName3(collection, source) {
  var srcKeys = Object.keys(source);

  // filter the collection
  return collection.filter(function(obj) {
    return srcKeys.map(function(key) {
      return obj.hasOwnProperty(key) && obj[key] == source[key];
    })
    .reduce(function(a, b) {
      return a && b;
    });
  });

  // filter through collection
  // map through all keys & return Boolean values based on the check conditions: both the key and its corresponding value must exist within the object we are filtering through
  // we reduce the mapped Boolean values to a single Boolean that indicates whether all srcKeys pass the condition checked above
  // This single Boolean will be used to filter through the collection
}

whatIsInAName([{ first: "Romeo", last: "Montague" }, { first: "Mercutio", last: null }, { first: "Tybalt", last: "Capulet" }], { last: "Capulet" });
