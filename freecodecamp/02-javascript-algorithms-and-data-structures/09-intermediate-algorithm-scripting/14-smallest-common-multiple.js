/*
Find the smallest common multiple of the provided parameters that can be evenly divided by both, as well as by all sequential numbers in the range between these parameters.

The range will be an array of two numbers that will not necessarily be in numerical order.

For example, if given 1 and 3, find the smallest common multiple of both 1 and 3 that is also evenly divisible by all numbers between 1 and 3. The answer here would be 6.
*/

// Initial naive solution left for posterity
// Caused potential infinite loop on freecodecamp for input [1, 13]
// Verified locally that it works for that input
function smallestCommonsNaive(arr) {
  /*
  determine number is prime
  then loop through numbers up to num determining if prime or not
  */
  console.log('===============================================')
  console.log(arr)
  // sorting is lexicographic order
  // so need a comparison function
  // https://medium.com/coding-at-dawn/how-to-sort-an-array-numerically-in-javascript-2b22710e3958
  arr.sort((a, b) => a-b)
  console.log(arr)

  // find multiple
  let multiplier = 1;
  let found = false;
  let numDivisible = 0;

  while (found === false) {
    for (let i = arr[0]; i <= arr[1]; i++) {
      var multiple = arr[0] * arr[1] * multiplier
      console.log('i:', i, '| multiple:', multiple)
      if (multiple % i != 0) {
        multiplier += 1;
        numDivisible = 0;
        break;
      } else {
        numDivisible += 1
      }
    }
    console.log('numDivisible:', numDivisible, arr[1] - arr[0] + 1)
    if (numDivisible == arr[1] - arr[0] + 1) {
      found = true
    }
  }
  return multiple;
}

console.log(smallestCommonsNaive([1, 13]));


function smallestCommons(arr) {
  const [min, max] = arr.sort((a, b) => a-b)
  const numDivisors = max - min + 1;

  // calculate upper bound to avoid inifinite while loop
  let upperBound = 1
  for (let i = min; i <= max; i++) {
    upperBound *= i;
  }
  console.log('upperBound:', upperBound)
  for (let multiple = max; multiple <= upperBound; multiple += max) {
    let numDivisible = 0;
    for (let i = min; i <= max; i++) {
      if (multiple % i == 0) {
        numDivisible += 1
      }
    }
    if (numDivisible === numDivisors) {
      console.log('multiple:', multiple)
      return multiple;
    }
  }
}

// Solution 1- Looping approach
function smallestCommons1(arr) {
  // Setup
  const [min, max] = arr.sort((a, b) => a - b);
  const numberDivisors = max - min + 1;
  // Largest possible value for SCM
  let upperBound = 1;
  for (let i = min; i <= max; i++) {
    upperBound *= i;
  }
  // Test all multiples of 'max'
  for (let multiple = max; multiple <= upperBound; multiple += max) {
    // Check if every value in range divides 'multiple'
    let divisorCount = 0;
    for (let i = min; i <= max; i++) {
      // Count divisors
      if (multiple % i === 0) {
        divisorCount += 1;
      }
    }
    if (divisorCount === numberDivisors) {
      return multiple;
    }
  }
}

// Solution 2 - ES5 looping
// Use ES6 syntax to condense logic in Solution 1
function smallestCommons2(arr) {
  // Setup
  const [min, max] = arr.sort((a, b) => a-b)
  const range = Array(max - min + 1)
    .fill(0)
    .map((_, i) => i + min);
  
  // Largest possible value for SCM
  const upperBound = range.reduce((prod, curr) => prod * curr);
  // Test all multiples of 'max'
  for (let multiple = max; multiple <= upperBound; multiple += max) {
    // Check if every value in range divides 'multiple'
    const divisible = range.every((value) => multiple % value === 0)
    if (divisible) {
      return multiple;
    }
  }
}

// Solution 3 - GCD and LCM
// Uses formulae and algorithms for Greatest Common Divisor
// and Least Common Multiple from Wikipedia to quickly
// compute the Smallest Common Multiple
function smallestCommons3(arr) {
  // Setup
  const [min, max] = arr.sort((a, b) => a-b)
  const range = Array(max - min + 1)
    .fill(0)
    .map((_, i) => i + min);
  
  // GCD of 2 numbers
  // https://en.wikipedia.org/wiki/Greatest_common_divisor#Euclid's_algorithm
  const gcd = (a, b) => (b === 0) ? a : gcd(b, a % b);

  // LCM of 2 numbers
  // https://en.wikipedia.org/wiki/Least_common_multiple#Using_the_greatest_common_divisor
  const lcm = (a, b) => a * b / gcd(a, b)

  // LCM of multiple numbers
  // https://en.wikipedia.org/wiki/Least_common_multiple#Other
  return range.reduce((multiple, curr) => lcm(multiple, curr))
}

// Solutiuon 4 - Prime factorization
function smallestCommons4(arr) {
  const primeFactors = {}
  const [min, max] = arr.sort((a, b) => a-b)
  for (let i = min; i <= max; i++ ) {
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
    multiple *= prime ** primeFactors[prime]
  }
  return multiple;
}

// Compute prime factors of a number
function getPrimeFactors(num) {
  const factors = {}
  for (let i = 2; i <= num; i++) {
    // Count occurences of factor
    // Note that composite values will not divide num
    while ((num % i) === 0) {
      factors[i] = (factors[i]) ? factors[i] + 1: 1;
      num /= i;
    }
  }
  return factors
}
