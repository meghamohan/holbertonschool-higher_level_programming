#!/usr/bin/node
// square inherits from rectangle
const rectangle = require('./4-rectangle').Rectangle;
// define square function
function Square (size) {
  rectangle.call(this, size, size);
}
// export the square function
exports.Square = Square;
