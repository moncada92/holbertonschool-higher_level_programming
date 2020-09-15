#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const numbers = [];
  process.argv.forEach(n => {
    numbers.push(n);
  });
  numbers.sort(function (a, b) {
    return a - b;
  });
  console.log(numbers[numbers.length - 2]);
}
