#!/usr/bin/node
exports.nbOccurences = (list, searchElement) => {
  let count = 0;
  let founds = list.indexOf(searchElement);
  while (founds !== -1) {
    count++;
    founds = list.indexOf(searchElement, founds + 1);
  }
  console.log(count);
};
