#!/usr/bin/node

const request = require('request');

const movieID = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movieID}/`;

let listOfActors;

const requestPromise = (url) => {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) reject(error);
      else resolve(body);
    });
  });
};

async function displayCharacters () {
  let movie = await requestPromise(url);
  movie = JSON.parse(movie);
  listOfActors = movie.characters;

  for (const actor of listOfActors) {
    let character = await requestPromise(actor);
    character = JSON.parse(character).name;
    console.log(character);
  }
}

displayCharacters();
