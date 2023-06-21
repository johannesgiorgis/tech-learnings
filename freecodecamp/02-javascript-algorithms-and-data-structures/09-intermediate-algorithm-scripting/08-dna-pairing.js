/*
The DNA strand is missing the pairing element. Take each character, get its pair, and return the results as a 2d array.
*/
function pairElement(str) {
    var result = [];
    var pairings = {
        'G': 'C',
        'A': 'T',
        'C': 'G',
        'T': 'A',
    };
    console.log('pairings:', pairings);
    console.log('str:', str);

    for (let c of str) {
        var pairs = [c];
        console.log(c);
        pairs.push(pairings[c]);
        result.push(pairs);
    }
    console.log('result:', result);
    return result;
}

// Solution 1
function pairElement1(str) {
    // Return each strand as an array of two elements, the original and the pair.
    var paired = [];

    // Function check which strand to pair.
    var search = function (char) {
        switch (char) {
            case "A":
                paired.push(['A', 'T']);
                break;
            case "T":
                paired.push(['T', 'A']);
                break;
            case "C":
                paired.push(['C', 'G']);
                break;
            case "G":
                paired.push(['G', 'C']);
                break;
        }
    };

    // Loops through the input and pair.
    for (var i = 0; i < str.length; i++) {
        search(str[i]);
    }

    return paired;
}


// Solution 2
function pairElement2(str) {
    // create object for pair lookup
    var pairs = {
        A: 'T',
        T: 'A',
        C: 'G',
        G: 'C',
    }

    // split string into array of characters
    var arr = str.split('');

    // map character to array of character and matching pair
    return arr.map(x => [x, pairs[x]]);
}

pairElement("GCG");
