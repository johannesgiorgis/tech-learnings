/*
Find the smallest common multiple of the provided parameters that can be evenly divided by both, as well as by all sequential numbers in the range between these parameters.

The range will be an array of two numbers that will not necessarily be in numerical order.

For example, if given 1 and 3, find the smallest common multiple of both 1 and 3 that is also evenly divisible by all numbers between 1 and 3. The answer here would be 6.

# Helpful Resources

- [Least Common Multiple Exercise - Factors and multiples (Khan Academy)](https://www.youtube.com/watch?v=znmPfDfsir8)
- [Prime factorization (Khan Academy)](https://www.youtube.com/watch?v=ZKKDTfHcsG0)
*/

function smallestCommons(arr) {
  const start = Math.min(...arr)
  const end = Math.max(...arr)
  var isDiv = false
  const numberDivisors = end - start + 1;

  var j = 1
  var result = 0
  while (!isDiv) {
    var multiple = end * j
    var divisor = 0
    for (var i = start; i <= end; i++) {
      if (multiple % i == 0) {
        divisor += 1;
      }
    }
    // how to determine where to end? Track number of divisors so far !
    if (divisor == numberDivisors) {
      result = multiple
      isDiv = true
    }
    j += 1
  }
  return result
}

// console.log(smallestCommons([1,5]));

/*
Solution 1 - Looping approach

In this solution, we check every multiple of the largest value in the range until we find a value 
that is divisible by every value in the range.

The upper bound for this loop is the product of all values in the provided range, because this 
number will be divisible by every value in the range.
*/

function smallestCommons1(arr) {
    // Setup
    const [min, max] = arr.sort((a, b) => a - b);
    const numberDivisors = max - min + 1;

    // Largest possible value for SCM
    let upperBound = 1;
    for (let i = min; i<=max; i++) {
        upperBound *= i
    }
    
    // Test all multiples of 'max'
    for (let multiple = max; multiple <= upperBound; multiple += max) {
        // Check if every value in range divides 'multiple'
        let divisorCount = 0
        for (let i = min; i<= max; i++) {
            // Count divisors
            if (multiple % i === 0) {
                divisorCount += 1
            }
        }
        if (divisorCount === numberDivisors) {
            return multiple
        }
    }
};

// console.log(smallestCommons1([1,5]));


/*
Solution 2 - ES6 looping

This solution uses ES6 syntax to condense the logic in Solution 1.
*/

function smallestCommons2(arr) {
    // Setup
    const [min, max] = arr.sort((a, b) => a - b);

    // create array with size of number of divisors and
    // populate with the range between min and max!
    const range = Array(max - min + 1)
        .fill(0)
        .map((_, i) => i + min);

    
    // Largest possible value for SCM
    const upperBound = range.reduce((prod, curr) => prod * curr);

    // Test all multiples of 'max'
    for (let multiple = max; multiple <= upperBound; multiple += max) {
        // Check if every value in range divides 'multiple'
        const divisible = range.every((value) => multiple % value == 0)
        if (divisible) {
            return multiple
        }
    }
}

// console.log(smallestCommons2([1,5]));


/*
Solution 3 - GCD and LCM

This solution uses formulae and algorithms for the Greatest Common Divisor and Least Common 
Multiple off of Wikipedia to compactly and quickly compute the Smallest Common Multiple.
*/

function smallestCommons3(arr) {
    // Setup
    const [min, max] = arr.sort((a, b) => a - b);
    const range = Array(max - min + 1)
        .fill(0)
        .map((_, i) => i + min);
    
    // GCD of two numbers
    // https://en.wikipedia.org/wiki/Greatest_common_divisor#Euclid's_algorithm
    const gcd = (a, b) => (b === 0) ? a : gcd(b, a % b);

    // LCM of two numbers
    // https://en.wikipedia.org/wiki/Least_common_multiple#Using_the_greatest_common_divisor
    const lcm = (a, b) => a * b / gcd (a, b);

    // LCM of multiple numbers
    // https://en.wikipedia.org/wiki/Least_common_multiple#Other
    return range.reduce((multiple, curr) => lcm(multiple, curr));
}

// console.log(smallestCommons3([1,5]));

/*
Solution 4 - Prime factorization

This solution uses a prime factorization of the numbers in the range to compute the smallest common 
multiple. In general, Solution 3 is much faster, but with a very large range or very large values, 
sometimes Solution 3 may trigger a recursion limit in some browsers.
*/

function smallestCommons4(arr) {
    const primeFactors = {}
    const [min, max] = arr.sort((a, b) => a - b);

    for (let i = min; i <= max; i++) {
        // Factorize number in range
        const currentFactors = getPrimeFactors(i);

        for (let prime in currentFactors) {
            // Add factor to set or update number of occurrences
            if (!primeFactors[prime] || currentFactors[prime] > primeFactors[prime]) {
                primeFactors[prime] = currentFactors[prime]
            }
        }
    }

    // Build SCM from factorization
    let multiple = 1;
    for (let prime in primeFactors) {
        multiple *= prime ** primeFactors[prime];
    }
    return multiple;
}

// Compute prime factors of a number
function getPrimeFactors(num) {
    const factors = {};
    for (let i = 2; i <= num; i++) {
        // Count occurences of factor
        // Note that composite values will not divide num
        while ((num % i) === 0) {
            factors[i] = (factors[i]) ? factors[i] + 1 : 1;
            num /= i;
        }
    }
    return factors;
}

console.log(smallestCommons4([1,5]));