#!/usr/local/bin/node

function secondBiggest (array) {
  if (array.length < 2) {
    return 0;
  }
  /* array.map() => Calls a defined callback function on each element of an array,
  and returns an array that contains the results.
  */
  const parsedArr = array.map(Number); // parsing array of str to numbers
  const sortedArr = parsedArr.sort(function (a, b) {
    return a - b;
  }); // in ascending order
  console.log(sortedArr);
  return sortedArr[array.length - 2];
}
console.log(secondBiggest(process.argv.slice(2))); // skip first two arguments
