#!/usr/bin/node
exports.addMeMaybe = (n, callback) => {
  ++n;
  callback(n);
};
