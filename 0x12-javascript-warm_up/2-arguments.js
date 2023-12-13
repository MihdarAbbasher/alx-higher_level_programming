#!/usr/bin/node

const x =  process.argv;
l = x.length;
if (l < 3) {
  console.log('No argument');
} else if (l == 3) {
  console.log(x[2]);
} else {
  console.log('Arguments found');
}
