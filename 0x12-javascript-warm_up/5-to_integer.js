#!/usr/bin/node
// A script that prints "My number: <first argument converted in integer>".

const myArg = Number(process.argv[2]);

if (isNaN(myArg)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + myArg);
}
