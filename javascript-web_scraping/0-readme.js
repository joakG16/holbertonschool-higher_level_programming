#!/usr/bin/node

const fs = require('fs');

/* The fs.readFile() method is used to read files on the computer */

const filename = process.argv[2];

fs.readFile(filename, 'utf-8', (err, data) => {
  err ? console.error(err) : console.log(data);
});
