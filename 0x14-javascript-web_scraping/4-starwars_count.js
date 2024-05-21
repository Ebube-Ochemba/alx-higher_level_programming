#!/usr/bin/node

// Import the request module
const request = require('request');

// Get the API URL from the command line arguments
const apiUrl = process.argv[2];

// Set character ID
const wedgeAntillesId = '18';

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

  const films = JSON.parse(body).results;
  let count = 0;

  films.forEach(film => {
    if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${wedgeAntillesId}/`)) {
      count++;
    }
  });

  console.log(count);
});
