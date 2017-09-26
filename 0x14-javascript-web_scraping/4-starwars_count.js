#!/usr/bin/node
const request = require('request');
let count = 0;
const searchUrl = 'https://swapi.co/api/people/18/';
const params = {
  url: process.argv[2],
  method: 'GET'
};
request(params, function (error, response, body) {
  if (!error) {
    const jsonObj = JSON.parse(body);
    for (let i of jsonObj.results) {
      for (let j of i.characters) {
        if (j.indexOf(searchUrl) >= 0) {
          count++;
        }
      }
    }
  }
  else
    console.log(error);
  console.log(count);
});
