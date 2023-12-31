#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let l = list.length;
  let res = 0;
  for (let i = 0; i < l; i++) {
    if (list[i] === searchElement) { res++; }
  }
  return (res);
}
