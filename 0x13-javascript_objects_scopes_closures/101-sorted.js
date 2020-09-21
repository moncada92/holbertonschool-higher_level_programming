#!/usr/bin/env node

const dict = require('./101-data').dict;

const newdict = {};
for (const [key, value] of Object.entries(dict)) {
  if (newdict[value] === undefined) {
    newdict[value] = [];
  }
  newdict[value].push(key);
}
console.log(newdict);
