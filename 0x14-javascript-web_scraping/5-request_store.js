#!/usr/bin/node
let url = process.argv[2];
let filePath = process.argv[3];
const fs = require('fs');
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(filePath, body, 'utf-8', function (error, data) {
      if (error) {
        console.log(error);
      }
    });
  }
});
