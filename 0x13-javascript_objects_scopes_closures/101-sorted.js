#!/usr/bin/node

const dict = require('./101-data').dict;

const newdict = {
  1: [],
  2: [],
  3: []
};

for (const key in dict) {
  if (dict[key] === 1) {
    newdict[1].push(key);
  } else if (dict[key] === 2) {
    newdict[2].push(key);
  } else if (dict[key] === 3) {
    newdict[3].push(key);
  }
}

console.log(newdict);
