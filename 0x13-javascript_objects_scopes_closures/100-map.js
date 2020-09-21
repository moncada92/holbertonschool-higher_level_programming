#!/usr/bin/node
const listN = require('./100-main').list;
const newList = [];
listN.map((index, el) => {
  newList.push(el * index);
});
console.log(listN);
console.log(newList);
