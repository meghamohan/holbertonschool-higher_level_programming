#!/usr/bin/node
exports.esrever = function (list) {
  const l = list.length;
  for (let i = 0, j = (l - 1); i < (l / 2); i++, j--) {
    [list[i], list[j]] = [list[j], list[i]];
  }
  return list;
};
