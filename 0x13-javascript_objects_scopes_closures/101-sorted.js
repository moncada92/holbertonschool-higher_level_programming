#!/usr/bin/env node

const dict = require('./101-data').dict;

const newdict = {
  1: [],
  2: [],
  3: []
};

for (const [key, value] of Object.entries(dict)) {
  newdict[value].push(key);
}
console.log(newdict);
