#!/usr/bin/node
// A script that prints the addition of 2 integers.

const num1 = Number(process.argv[2]);
const num2 = Number(process.argv[3]);

function add (a, b) {
  return (a + b);
}

console.log(add(num1, num2));
