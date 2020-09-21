#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (!c) {
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
