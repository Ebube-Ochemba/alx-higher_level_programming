#!/usr/bin/node
// A script that prints the first argument passed to it.

if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  const myarg = process.argv[2];
  console.log(myarg);
}
