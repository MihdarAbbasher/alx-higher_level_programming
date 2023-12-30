#!/usr/bin/node
exports.converter = function (base) {
  return function (d) {
    return d.toString(base);
  };
};
