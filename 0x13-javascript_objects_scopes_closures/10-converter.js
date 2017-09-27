#!/usr/bin/node
exports.converter = function (base = 10) {
  return function (num) {
    return num.toString(base);
  };
};
