/*
Convert the characters &, <, >, " (double quote), and ' (apostrophe), in a string to their corresponding HTML entities.
*/

function convertHTML(str) {
    const result = str
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&apos;');
    console.log(result);
    return result;
}
  
convertHTML("Dolce & Gabbana");

// Solution 1
function convertHTML1(str) {
    var temp = str.split('');

    for (var i = 0; i < temp.length; i++) {
        switch (temp[i]) {
            case "<":
              temp[i] = "&lt;";
              break;
            case "&":
              temp[i] = "&amp;";
              break;
            case ">":
              temp[i] = "&gt;";
              break;
            case '"':
              temp[i] = "&quot;";
              break;
            case "'":
              temp[i] = "&apos;";
              break;
          }
    }

    temp = temp.join("");
    return temp;
}

// Solution 2
function convertHTML2(str) {
    const htmlEntities = {
        "&": "&amp;",
        "<": "&lt;",
        ">": "&gt;",
        '"': "&quot;",
        "'": "&apos;"
    }
    return str.replace(/\([&<>\"']/g, match => htmlEntities[match]);
}

// Solution 3
function convertHTML3(str) {
    const htmlEntities = {
        "&": "&amp;",
        "<": "&lt;",
        ">": "&gt;",
        '"': "&quot;",
        "'": "&apos;"
    }
    return str
        .split("")
        .map(entity => htmlEntities[entity] || entity)
        .join("");
}
