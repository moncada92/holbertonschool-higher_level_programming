#!/usr/bin/node
const numbers = [];
process.argv.forEach(n => {
  numbers.push(n);
});
numbers.sort(function (a, b) {
  return a - b;
});
console.log(numbers[numbers.length - 2]);
