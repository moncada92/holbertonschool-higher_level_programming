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
      const links = body.characters;
      getPeple(links, 0);
    }
  }
});

function getPeple (link, idx) {
  if (idx === link.length) { return; }
  request({
    url: link[idx],
    json: true
  }, (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      if (response.statusCode === 200) {
        console.log(body.name);
        getPeple(link, idx + 1);
      }
    }
  });
}
