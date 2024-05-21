#!/usr/bin/node

// Import the request module
const request = require('request');

// Get the URL from the command line arguments
const url = process.argv[2];

// Use the get method of the request module to send a GET request to the URL
request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
