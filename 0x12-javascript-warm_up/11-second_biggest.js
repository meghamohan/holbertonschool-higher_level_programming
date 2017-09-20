#!/usr/bin/node

const arr = process.argv.splice(2);
if (arr.length < 2) {
  console.log(0);
} else {
  arr.sort();
  let length = arr.length;
  console.log(arr[length - 2]);
}
