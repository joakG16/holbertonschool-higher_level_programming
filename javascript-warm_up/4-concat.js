#!/usr/bin/node
const args = process.argv; // Array of arguments
const empty = '';

console.log(empty.concat(args[2], ' is ', args[3])); // Concatenate the first and second argument
