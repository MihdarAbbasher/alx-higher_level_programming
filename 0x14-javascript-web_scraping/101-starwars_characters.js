#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;
let chars = [];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const res = JSON.parse(body);
  chars = res.chars;
  getchars(0);
});

const getchars = (index) => {
  if (index === chars.length) {
    return;
  }
  request(chars[index], (error, response, body) => {
    if (error) {
      console.log(error);
      return;
    }
    const characterData = JSON.parse(body);
    console.log(characterData.name);
    getchars(index + 1);
  });
};
