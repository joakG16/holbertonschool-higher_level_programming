#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const symb = 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(symb.repeat(this.width));
    }
  }

  rotate () {
    [this.height, this.width] = [this.width, this.height]; // Destructuring assignment
  }

  double () {
    this.width *= 2; // multiply and assign
    this.height *= 2;
  }
};
