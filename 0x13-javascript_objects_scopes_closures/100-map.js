#!/usr/bin/node
// A script that imports an array and computes a new array.

const { list } = require('./100-data');

const newList = list.map((x, idx) => x * idx);

console.log(list);
console.log(newList);
