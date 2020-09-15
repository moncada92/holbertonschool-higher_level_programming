#!/usr/bin/node
if (process.argv[2] != null && isNaN(process.argv[2]) === false) {
  console.log(`my numer: ${parseInt(process.argv[2])}`);
} else {
  console.log('Not a number');
}
