#!/usr/bin/node
const num = process.argv[2];

function factorial (n) {
  if (n === 1) {
    return 1;
  } else {
    return (factorial(n - 1) * n);
  }
}

if (num === undefined || isNaN(parseInt(num))) {
  console.log(1);
} else {
  console.log(factorial(parseInt(num)));
}
