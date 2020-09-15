#!/usr/bin/node
if (process.argv[2] != null && isNaN(process.argv[2]) === false) {
  let x = process.argv[2];
  let y = 0;
  let letters = '';
  if (x > 0) {
    while (x) {
      while (x > y) {
        letters += 'X';
        y++;
      }
      console.log(letters);
      x--;
    }
  }
} else {
  console.log('Missing size');
}
