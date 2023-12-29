#!/usr/bin/node
const { argv } = require('process');
const num = Number(argv[2]);
const display_x_times = (x) => {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
};
isNaN(num)
  ? (console.log('Missing number of occurrences'))
  : (display_x_times(num));
