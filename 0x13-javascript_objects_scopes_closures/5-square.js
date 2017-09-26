#!/usr/bin/node
// square inherits from rectangle
const Rectangle = require('./4-rectangle').Rectangle;
// define square function
function Square (size) {
  Rectangle.call(this, size, size);
}
// export the square function
exports.Square = Square;
