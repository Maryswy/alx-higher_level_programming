#!/usr/bin/node

const fs = require('fs');
const request = require('request');

// Get command line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Make request to URL
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // Write response body to file
  fs.writeFile(filePath, body, { encoding: 'utf-8' }, (error) => {
    if (error) {
      console.error(error);
      return;
    }

    console.log(`File saved to ${filePath}`);
  });
});
