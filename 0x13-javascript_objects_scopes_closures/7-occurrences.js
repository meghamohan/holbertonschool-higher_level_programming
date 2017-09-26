#!/usr/bin/node
exports.nbOccurences = function (list, search_element) {
  let c = 0;
  for (let i = 0; i < list.length; i++) {
    if (search_element === list[i]) {
      c++;
    }
  }
  return c;
};
