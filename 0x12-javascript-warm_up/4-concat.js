#!/usr/bin/node
// A script that prints two arguments passed to it, in the following format: "is".

const myArgs = process.argv;

console.log(myArgs[2] + ' is ' + myArgs[3]);
