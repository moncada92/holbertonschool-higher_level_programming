#!/usr/bin/node

const fs = require('fs');

const cisfun = fs.readFileSync(process.argv[2], 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    return data;
  }
});

console.log(cisfun);
