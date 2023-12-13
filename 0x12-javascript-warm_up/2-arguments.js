#!/usr/bin/node

const x = process.argv;
const l = x.length;
if (l < 3) {
  console.log('No argument');
} else if (l === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
