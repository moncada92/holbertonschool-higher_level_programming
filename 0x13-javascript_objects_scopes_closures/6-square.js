#!/usr/bin/node

const _Squere = require('./5-square');

class Square extends _Squere {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let tmp = '';
    for (let i = 0; i < this.width; i++) {
      for (let j = 0; j < this.width; j++) {
        tmp += c;
      }
      console.log(tmp);
      tmp = '';
    }
  }
}

module.exports = Square;
