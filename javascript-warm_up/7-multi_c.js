#!/usr/bin/node

const str = 'C is fun';
const i = process.argv[2];

if (!parseInt(i)) {
  console.log('Missing number of occurrences');
}
for (let j = 0; j < i; j++) {
  console.log(str);
}
