#!/usr/bin/node
// A class Rectangle that defines a rectangle.

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let idx = 0; idx < this.height; idx++) {
      let row = '';
      for (let idy = 0; idy < this.width; idy++) {
        row += 'X';
      }
      console.log(row);
    }
  }
}

module.exports = Rectangle;

/*
 * print () {
 * for (let i = 0; i < this.height; i++) {
 * console.log('X'.repeat(this.width));
 * }
 * }
 */
