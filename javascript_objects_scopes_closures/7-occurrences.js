#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const value of list) {
    value === searchElement ? count += 1 : count += 0; // condition ? exprIfTrue : exprIfFalse
  }
  return count;
};
