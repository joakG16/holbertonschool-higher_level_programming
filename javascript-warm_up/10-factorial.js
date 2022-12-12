#!/usr/bin/node
function factorial (n) {
  if (!n) { // Factorial of NaN
    return 1;
  }
  return n * factorial(n - 1);
}

console.log(factorial(process.argv[2]));
