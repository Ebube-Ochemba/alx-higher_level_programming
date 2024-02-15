#!/usr/bin/node
// A function that returns the reversed version of a list.

exports.esrever = function (list) {
  const revList = [];

  for (const idx in list) {
    revList.unshift(list[idx]);
  }
  return (revList);
};
