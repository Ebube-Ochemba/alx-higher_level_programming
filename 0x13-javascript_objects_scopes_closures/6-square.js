#!/usr/bin/node
// A class Square that defines a square and inherits from Square.

const Square5 = require('./5-square');

class Square extends Square5 {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let idx = 0; idx < this.height; idx++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}

module.exports = Square;
