#!/usr/bin/node

const request = require('request');
let count = 0;
const id = '18';

const url = `${process.argv[2]}`;
request({
  url: url,
  json: true
}, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  if (response.statusCode === 200) {
    body.results.forEach(element => {
      element.characters.forEach(el => {
        if (el.indexOf(id) >= 0) {
          count++;
        }
      });
    });
    console.log(count);
  }
});
