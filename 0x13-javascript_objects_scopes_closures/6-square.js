#!/usr/bin/node
const square = require('./5-square').Square;

function Square (size) {
  square.call(this, size);
}
Square.prototype.charPrint = function (a = 'X') {
  for (let i = 0; i < this.height; i += 1) {
    console.log(a.repeat(this.width));
  }
};
exports.Square = Square;
