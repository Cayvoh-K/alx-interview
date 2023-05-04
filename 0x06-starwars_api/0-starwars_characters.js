#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Error: Please specify a movie ID as the first argument');
  process.exit(1);
}

const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request(url, { json: true }, (err, res, body) => {
  if (err) {
    console.error(`Error: ${err.message}`);
    process.exit(1);
  }

  if (res.statusCode !== 200) {
    console.error(`Error: API returned status code ${res.statusCode}`);
    process.exit(1);
  }

  const characters = body.characters;

  characters.forEach(characterUrl => {
    request(characterUrl, { json: true }, (err, res, body) => {
      if (err) {
        console.error(`Error: ${err.message}`);
        return;
      }

      if (res.statusCode !== 200) {
        console.error(`Error: API returned status code ${res.statusCode}`);
        return;
      }

      console.log(body.name);
    });
  });
});
