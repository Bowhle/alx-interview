#!/usr/bin/node

const request = require('request');

/**
 * Fetch JSON data from a provided URL using a Promise.
 * @param {string} url - The API endpoint to retrieve data from.
 * @returns {Promise<Object>} - A Promise resolving to the parsed JSON response.
 */
function fetchJSON (url) {
  return new Promise((resolve, reject) => {
    request(url, (err, res, body) => {
      if (err) reject(err);
      else resolve(JSON.parse(body));
    });
  });
}

/**
 * Retrieve and display the names of characters in a Star Wars film.
 * Characters are printed in the same order as they appear in the film.
 * @param {string} movieId - The ID of the Star Wars film to fetch.
 */
async function fetchAndPrintCharacters (movieId) {
  try {
    const film = await fetchJSON(`https://swapi-api.alx-tools.com/api/films/${movieId}`);
    const characters = film.characters;

    for (const url of characters) {
      const character = await fetchJSON(url);
      console.log(character.name);
    }
  } catch (err) {
    console.error(err);
  }
}

// Entry point: check for movie ID input and execute main logic
const movieId = process.argv[2];
if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

fetchAndPrintCharacters(movieId);
