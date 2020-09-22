#!/usr/bin/node
const request = require('request');
const url = `${process.argv[2]}`;

request({
  url: url,
  json: true
}, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    if (response.statusCode === 200) {
      const store = {};
      body.forEach(element => {
        const { userId, completed } = element;
        if (completed) {
          if (store[userId]) {
            store[userId]++;
          } else {
            store[userId] = 1;
          }
        }
      });
      console.log(store);
    }
  }
});
