#!/usr/bin/node

function secondBiggest (list) { 
  if (list.length < 2) {
    return 0;
  }
  list.sort(function (a, b) {
    return a - b;
  });
  return list[list.length - 2];
}
console.log(secondBiggest(process.argv.slice(2)));
