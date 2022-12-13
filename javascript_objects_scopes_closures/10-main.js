#!/usr/bin/node
const converter = require('./10-converter').converter;

/* Calling converter() function, which will return
the function inside that handles the conversion */
let myConverter = converter(10);

/* applying "returned function", stored in myConverter, to the
numbers given */
console.log(myConverter(2));
console.log(myConverter(12));
console.log(myConverter(89));

myConverter = converter(16);

console.log(myConverter(2));
console.log(myConverter(12));
console.log(myConverter(89));
