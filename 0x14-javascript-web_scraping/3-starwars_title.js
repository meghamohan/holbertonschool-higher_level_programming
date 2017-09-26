#!/usr/bin/node
const request = require('request');
const params = {
  url: 'http://swapi.co/api/films/' + process.argv[2],
  method: 'GET'
};
request(params, function (error, response, body) {
  if (!error) {
    const jsonObj = JSON.parse(body);
    console.log(jsonObj['title']);
  }
});
