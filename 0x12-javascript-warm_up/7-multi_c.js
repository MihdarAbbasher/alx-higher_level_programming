#!/usr/bin/node
const { argv } = require('process');
const num = Number(argv[2]);
const displayXtimes = (x) => {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
};
isNaN(num)
  ? (console.log('Missing number of occurrences'))
  : (displayXtimes(num));
