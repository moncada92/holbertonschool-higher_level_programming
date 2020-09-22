#!/usr/bin/node
const request = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}/`;

request({
  url: url,
  json: true
}, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    if (response.statusCode === 200) {
      body.characters.forEach(element => {
        request({
          url: element,
          json: true
        }, (error, response, body) => {
          if (error) {
            console.log(error);
          } else {
            if (response.statusCode === 200) {
              console.log(body.name);
            }
          }
        });
      });
    }
  }
});
