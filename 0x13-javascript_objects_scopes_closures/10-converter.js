#!/usr/bin/node
exports.converter = base => {
  return function myconverter (num) { return num.toString(base); };
};
