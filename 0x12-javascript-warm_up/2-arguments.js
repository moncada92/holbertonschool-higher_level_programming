#!/usr/bin/node
const size = process.argv.length;
if (size === 2) {
  console.log('No argument');
} else if (size === 3) {
  console.log('Argument found');
} else if (size > 3) {
  console.log('Arguments found');
}
