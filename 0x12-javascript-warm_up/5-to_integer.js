#!/usr/bin/node
if (isNaN(process.argv[2]) === false) {
  console.log(`my numer: ${parseInt(process.argv[2], 10)}`);
} else {
  console.log('Not a number');
}
