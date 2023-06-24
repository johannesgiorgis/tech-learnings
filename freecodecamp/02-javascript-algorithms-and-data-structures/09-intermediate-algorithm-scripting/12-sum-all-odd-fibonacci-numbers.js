/*
Given a positive integer num, return the sum of all odd Fibonacci numbers that are less than or equal to num.

The first two numbers in the Fibonacci sequence are 0 and 1. Every additional number in the sequence is the sum of the two previous numbers. The first seven numbers of the Fibonacci sequence are 0, 1, 1, 2, 3, 5 and 8.

For example, sumFibs(10) should return 10 because all odd Fibonacci numbers less than or equal to 10 are 1, 1, 3, and 5.
*/

function sumFibs(num) {
    let first = 0;
    let second = 1;
    let sum = 0;
    let sumOdd = second;
  
    while (sum < num) {
      // console.log('B:', sum, sumOdd)
  
      sum = first + second
      first = second
      second = sum
      if (second % 2 == 1 && second <= num) {
        sumOdd += second
      }
      // if (first % 2 == 1 && first <= num) {
      //   sumOdd += first
      // }
      // console.log('A:', sum, sumOdd)
    }
    console.log(sum, '<', num, '|', sumOdd)
    return sumOdd;
}
  
sumFibs(4);

// Solution 1
function sumFibs1(num) {
    let prevNumber = 0;
    let currNumber = 1;
    let result = 0;
    while (currNumber <= num) {
        if (currNumber % 2 !== 0) {
            result += currNumber;
        }
        currNumber += prevNumber;
        prevNumber = currNumber - prevNumber;
    }
    return result;
}

// Solution 2
function sumFibs2(num) {
    if (num <= 0) return 0;

    const arrFib = [1, 1];
    let nextFib = 0;

    // We put the new Fibonacci numbers to the front so
    // we don't need to calculate the length of the array on each
    // iteration.
    while ((nextFib = arrFib[0] + arrFib[1]) <= num) {
        arrFib.unshift(nextFib);
    }

    // We filter the array to get the odd numbers and reduce them to get their sum.
    return arrFib.filter(x => x % 2 != 0).reduce((a, b) => a + b)
}

// Solution 3
function sumFibs3(num) {
    // Every third Fibonacci number is even
    // and the rest are odd
    let f0 = 0;
    let f1 = 1;
    let f2 = 1;

    // Generate triples until num is reached
    let sum = 0;
    while (f1 <= num) {
        // Update sum
        sum += f1;
        if (f2 <= num) sum += f2;

        // Compute next three Fibonacci numbers
        [f0, f1] = [f1 + f2, f2 + (f1 + f2)];
        f2 = f0 + f1;
    }

    return sum;
}