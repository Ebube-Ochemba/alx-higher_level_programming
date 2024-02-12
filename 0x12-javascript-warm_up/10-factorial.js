#!/usr/bin/node
// A script that computes and prints a factorial.

const num = Number(process.argv[2]);

function factorial (n) {
  if (n === 0 || n === 1 || isNaN(n)) {
    return (1);
  } else {
    return (n * (factorial(n - 1)));
  }
}

console.log(factorial(num));
