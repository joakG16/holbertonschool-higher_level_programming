#!/usr/bin/node
const symb = 'X';
const i = process.argv[2];

if (i && parseInt(i)) {
  for (let j = 0; j < i; j++) {
    console.log(symb.repeat(i)); // repeats 'i' times the string 'X' in the line
  }
} else {
  console.log('Missing size');
}
