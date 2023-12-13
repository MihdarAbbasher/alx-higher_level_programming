#!/usr/bin/node

const x = process.argv.slice(2);
if (arrayIsEmpty(x)) {
  console.log('No argument');
} else {
  console.log('No argument');
  x.foreach(v, function(){
    console.log(v);
  })
}
