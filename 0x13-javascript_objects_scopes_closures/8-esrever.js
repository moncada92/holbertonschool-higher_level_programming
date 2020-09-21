#!/usr/bin/node
exports.esrever = list => {
  let size = list.length - 1;
  const newList = [];
  while (size !== -1) {
    newList.push(list[size]);
    size--;
  }
  return newList;
};
