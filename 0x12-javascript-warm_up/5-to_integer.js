#!/usr/bin/node
const value = process.argv[2];
if (isNaN(value) === false) {
  console.log(parseInt(value, 10));
} else {
  console.log('Not a number');
}
