#!/usr/bin/node

const fs = require('fs');

/*
The first argument is the file path
The content of the file must be read in utf-8
If an error occurred during the reading, print the error object
*/

const filename = process.argv[2]; // The fs.readFile() method is used to read files on the computer

fs.readFile(filename, 'utf-8', (err, data) => {
  err ? console.error(err) : console.log(data);
});
