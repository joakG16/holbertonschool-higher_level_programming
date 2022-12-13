#!/usr/bin/node
let previous = 0;
exports.logMe = function (item) {
  console.log(previous + ': ' + item);
  previous += 1;
};
