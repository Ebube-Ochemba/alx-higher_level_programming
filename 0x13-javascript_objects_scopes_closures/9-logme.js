#!/usr/bin/node
// A function that prints the number of arguments already printed and the new argument value.

let ClosureCheck = 0;
exports.logMe = function (item) {
  console.log(ClosureCheck + ': ' + item);
  ClosureCheck++;
};
