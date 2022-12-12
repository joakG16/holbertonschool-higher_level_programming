#!/usr/bin/node

function secondBiggest (array) {
  if (array.length < 2) {
    return 0;
  }
  const sortedArr = array.sort(); // in ascending order
  return sortedArr[array.length - 2];
}
console.log(secondBiggest(process.argv.slice(2))); // skip first two arguments
