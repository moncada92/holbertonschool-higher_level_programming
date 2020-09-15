#!/usr/bin/node
if (process.argv[2] != null && isNaN(process.argv[2]) === false) {
  let x = parseInt(process.argv[2]);
  if (x > 0) {
    while (x) {
      console.log('C is fun');
      x--;
    }
  }
} else {
  console.log('Missing number of occurrences');
}
