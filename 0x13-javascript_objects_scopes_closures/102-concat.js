#!/usr/bin/node

const fs = require('fs');

const fileA = fs.readFileSync(process.argv[2], 'utf-8', (err, data) => {
  if (err) {
    console.log('error: ', err);
  } else {
    return data;
  }
});

const fileB = fs.readFileSync(process.argv[3], 'utf-8', (err, data) => {
  if (err) {
    console.log('error: ', err);
  } else {
    return data;
  }
});

const fileC = `${fileA}${fileB}`;

fs.writeFile(process.argv[4], fileC, err => {
  if (err) {
    console.log('error write the file');
  }
});
