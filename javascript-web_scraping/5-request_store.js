#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const loreipsumAPI = process.argv[2];
const filename = process.argv[3];

request(loreipsumAPI, 'utf-8', (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    // const parseddata = JSON.parse(); // recieving not-parseable data
    // res.body === body = true
    const text = body;
    fs.writeFile(filename, text, 'utf-8', err => {
      if (err) {
        console.error(err);
      }
    });
  }
});
