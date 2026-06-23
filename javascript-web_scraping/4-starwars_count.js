#!/usr/bin/node
const request = require('request');
request(process.argv[2], (err, response, body) => {
  const films = JSON.parse(body).results;
  const count = films.filter(film =>
    film.characters.some(url => url.includes('/18/'))
  ).length;
  console.log(count);
});
