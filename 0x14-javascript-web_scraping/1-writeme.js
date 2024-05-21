#!/usr/bin/node

// Import the file system module
const fs = require('fs');

// Get the file path and string to write from the command line arguments
const file = process.argv[2];
const content = process.argv[3];

// Use the readFile function to read the file asynchronously
fs.writeFile(file, content, 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  }
});
