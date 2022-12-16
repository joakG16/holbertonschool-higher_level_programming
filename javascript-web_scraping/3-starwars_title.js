#!/usr/bin/node

const request = require('request');

const filmID = process.argv[2];

request(`https://swapi-api.hbtn.io/api/films/${filmID}`, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    const parseddata = JSON.parse(body);
    console.log(parseddata.title);
  }
});
