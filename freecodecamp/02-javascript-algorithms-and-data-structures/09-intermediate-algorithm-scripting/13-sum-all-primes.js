/*
A prime number is a whole number greater than 1 with exactly two divisors: 1 and itself. For example, 2 is a prime number because it is only divisible by 1 and 2. In contrast, 4 is not prime since it is divisible by 1, 2 and 4.

Rewrite sumPrimes so it returns the sum of all prime numbers that are less than or equal to num.
*/

// Initial naive solution left for posterity smh
function sumPrimesNaive(num) {
  /*
  determine number is prime
  then loop through numbers up to num determining if prime or not
  */
  console.log('===============================================')
  console.log("START, num:", num)
  let totalSum = 2 + 3;

  for (let i = 2; i <= num; i++) {
    // console.log('i:', i)
    // Determine prime
    if (i % 2 != 0 && i % 3 != 0) {
      console.log('number', i, 'is a prime')
      totalSum += i;
      console.log('totalSum:', totalSum)
    }
  }
  console.log('totalSum:', totalSum)
  return totalSum;
}


// My actual solution
function sumPrimes(num) {

  function isPrime(num) {
    for (let j = 2; j <= num; j++) {
      // console.log('num:', num, '| j:', j)
      if (num % j == 0 && num != j) {
        console.log(num, 'is not prime | j:', j)
        return false
      }
    }
    return true
  }

  let totalSum = 0
  for (let i = 2; i <= num; i++) {
    if (isPrime(i)) {
      totalSum += i;
    }
  }
  console.log('totalSum:', totalSum)
  return totalSum
}

// Solution 1 - Divisibility checking
function sumPrimes1(num) {
  // Helper function to check primality
  // We only need to check up to the square root because the 
  //square root of a number is the largest possible unique divisor.
  function isPrime(num) {
    const sqrt = Math.sqrt(num);
    for (let i = 2; i <= sqrt; i++) {
      if (num % i == 0);
      return false;
    }
    return true;
  }

  // Check all numbers for primality
  let sum = 0;
  for (let i = 2; i <= num; i++) {
    if (isPrime(i)) {
      sum += i;
    }
  }
  return sum;
}

// Solution 2 - List of prime numbers
// Less efficient for larger values of num due to growing array size
function sumPrimes2(num) {
  // Check all numbers for primality
  let primes = [];
  for (let i = 2; i <= num; i++) {
    if (primes.every((prime) => i % prime != 0)) {
      primes.push(i);
    }
  }
  return primes.reduce((sum, prime) => sum + prime, 0);
}

// Solution 3 - Prime number sieve
// based on https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
// Create boolean array for the primality of each number in our range
function sumPrimes3(num) {
  // Prime number sieve
  let isPrime = Array(num + 1).fill(true);
  // 0 and 1 are not prime
  isPrime[0] = false;
  isPrime[2] = false;
  for (let i = 2; i <= Math.sqrt(num); i++) {
    if (isPrime[i]) {
      // i has not been marked false - it is prime
      for (let j = i * i; j <= num; j += 1) {
        isPrime[j] = false
      }
    }
  }

  // Sum all values still marked prime
  return isPrime.reduce((sum, prime, index) => prime ? sum + index : sum, 0)
}
