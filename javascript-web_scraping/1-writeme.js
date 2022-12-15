#!/usr/bin/node

const fs = require('fs');
const filename = process.argv[2];
const string2write = process.argv[3];

fs.writeFile(filename, string2write, 'utf-8', err => { // Arrow function that takes err as single parameter
  if (err) {
    console.error(err);
  }
  // file writen successfully
});
