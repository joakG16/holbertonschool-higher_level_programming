#!/usr/bin/node

const request = require('request');

const apiURL = process.argv[2]; // new API URL https://swapi-api.alx-tools.com/api/films

request(apiURL, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    const parseddata = JSON.parse(body);
    const films = parseddata.results;
    let count = 0;
    for (const film of films) { // entering each film object in the films array
      for (const character of film.characters) { // entering current film's array of string of present-character's URLs
        if (character.endsWith('/18/')) { // if the current URL of the charcter in the current film mactches
          // for testing, use the updated character API URL: https://swapi-api.alx-tools.com/api/people/18/
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
