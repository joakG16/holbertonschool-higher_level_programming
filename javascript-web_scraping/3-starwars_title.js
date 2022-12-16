#!/usr/local/bin/node

const request = require('request');

const filmID = process.argv[2];

request(`https://swapi-api.hbtn.io/api/films/${filmID}`, (err, res) => {
  if (err) {
    console.error(err);
  } else {
    console.log('code: ' + res.title);
  }
});
