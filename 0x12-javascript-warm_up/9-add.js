#!/usr/bin/node

function add (a, b) {
  console.log(a + b);
}

let arr = process.argv.slice(2);
if (!arr || !parseInt(arr[0]) || !parseInt(arr[1])) {
  console.log('NaN');
} else {
  add(parseInt(arr[0]), parseInt(arr[1]));
}
