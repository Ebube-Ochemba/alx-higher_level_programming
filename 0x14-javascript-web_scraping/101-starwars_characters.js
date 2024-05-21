#!/usr/bin/node

// Import the request module
const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

// Construct the API URL using the movie ID
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Use the get method of the request module to send a GET request to the API URL
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  if (response.statusCode !== 200) {
    console.error(`Error: ${response.statusCode}`);
    return;
  }

  const film = JSON.parse(body);
  const characters = film.characters;
  const characterNames = [];

  // Function to fetch character names in order
  const fetchCharacterName = (index) => {
    if (index >= characters.length) {
      // Print character names when all are fetched
      characterNames.forEach(name => console.log(name));
      return;
    }
    request.get(characters[index], (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }
      if (response.statusCode !== 200) {
        console.error(`Error: ${response.statusCode}`);
        return;
      }
      const character = JSON.parse(body);
      characterNames.push(character.name);
      // Fetch next character
      fetchCharacterName(index + 1);
    });
  };

  // Start fetching character names
  fetchCharacterName(0);
});
