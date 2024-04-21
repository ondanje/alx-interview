#!/usr/bin/node

const request = require('request');

function getMovieCharacters (movieId) {
  const url = `https://swapi.dev/api/films/${movieId}/`;
  request(url, (error, response, body) => {
    if (error) {
      console.error('Error fetching data:', error);
      return;
    }
    if (response.statusCode !== 200) {
      console.error('Error fetching movie data: ', response.statusCode);
      return;
    }
    const movieData = JSON.parse(body);
    const charactersUrls = movieData.characters;
    charactersUrls.forEach(charactersUrl => {
      request(charactersUrl, (charError, charResponse, charBody) => {
        if (charError) {
          console.error('Error fetching character data:', charError);
          return;
        }
        if (charResponse.statusCode !== 200) {
          console.error('Error fetching character data. Status code:', charResponse.statusCode);
          return;
        }
        const characterData = JSON.parse(charBody);
        console.log(characterData.name);
      });
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
