#!/usr/bin/node
exports.callMeMoby = (n, callback) => {
  for (let i = 0; i < n; i++) {
    callback();
  }
};
