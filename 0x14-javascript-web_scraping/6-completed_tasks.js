#!/usr/bin/node
const request = require('request');
const url = `${process.argv[2]}`;
let count = 0;

request({
  url: url,
  json: true
}, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  if (response.statusCode === 200) {
    const store = {};
    body.forEach(element => {
      const { userId, completed } = element;
      if (store[userId] === undefined) {
        count = 0;
        store[userId] = count;
      }
      if (completed) {
        count++;
        store[userId] = count;
      }
    });
    console.log(store);
  }
});
