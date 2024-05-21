#!/usr/bin/node

// Import the request module
const request = require('request');

// Import the file system module
const fs = require('fs');

// Get the API URL from the command line arguments
const url = process.argv[2];

// Get the path to store the body response from the command line arguments
const filePath = process.argv[3];

// Use the get method of the request module to send a GET request to the API URL
request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  if (response.statusCode !== 200) {
    console.error(`Error: ${response.statusCode}`);
    return;
  }

  fs.writeFile(filePath, body, 'utf8', (err) => {
    if (err) {
      console.error(err);
    }
  });
});
