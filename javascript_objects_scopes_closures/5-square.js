#!/usr/bin/node
const Rectangle = require('./4-rectangle');

/*
 * Create a Square class that inherits from Rectangle and implement its class constructor
 */
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size); // width === height
  }
};
