#!/usr/bin/node
// A script that prints 3 lines, but by using an array of string and a loop.

const mylist = ['C is fun', 'Python is cool', 'JavaScript is amazing'];

for (const arg in mylist) {
  console.log(mylist[arg]);
}
