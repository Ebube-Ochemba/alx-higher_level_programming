#!/usr/bin/node

// Import the file system module
const fs = require('fs');

// Get the file path from the command line arguments
const filePath = process.argv[2];

// Use the readFile function to read the file asynchronously
fs.readFile(filePath, 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
