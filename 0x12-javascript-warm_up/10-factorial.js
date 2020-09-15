#!/usr/bin/node
const value = process.argv[2];

function factorial (n) {
  if (isNaN(n) === true || n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

console.log(`${factorial(value)}`);
