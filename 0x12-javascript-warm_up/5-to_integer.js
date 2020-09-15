#!/usr/bin/node
const value = process.argv[2];
if (isNaN(Number(value))) {
  console.log('Not a number');
} else {
  console.log(`My number: ${parseInt(value, 10)}`);
}
