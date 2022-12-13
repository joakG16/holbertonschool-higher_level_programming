#!/usr/bin/node

exports.esrever = function (list) {
  const RevArr = [];
  for (let i = list.lenght - 1; i >= 0; i--) {
    RevArr.push(list[i]);
  }
  return RevArr;
};
