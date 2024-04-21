#!/usr/bin/node

const request = require('request');

function fetchCharacterData (characterUrl) {
  return new Promise((resolve, reject) => {
    request(characterUrl, (error, response, body) => {
      if (error || response.statusCode !== 200) {
        reject(error || new Error(`Failed to fetch character data for URL: ${characterUrl}`));
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}

function getMovieCharacters (movieId) {
  const url = `https://swapi.dev/api/films/${movieId}/`;
  request(url, (error, response, body) => {
    if (error || response.statusCode !== 200) {
      console.error('Error fetching movie data:', error || response.statusCode);
      return;
    }

    const movieData = JSON.parse(body);
    const charactersUrls = movieData.characters;
    const characterPromises = charactersUrls.map(characterUrl => fetchCharacterData(characterUrl));

    Promise.all(characterPromises)
      .then(characters => {
        characters.forEach(character => {
          console.log(character.name);
        });
      })
      .catch(error => {
        console.error('Error fetching character data:', error);
      });
  });
}

const args = process.argv.slice(2);
if (args.length !== 1) {
  console.log('Usage: node script.js <movieId>');
} else {
  const movieId = args[0];
  getMovieCharacters(movieId);
}
