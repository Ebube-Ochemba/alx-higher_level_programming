#!/usr/bin/node

const { dict } = require('./101-data');

const newDict = {};

let tmp = [];
for (const [key, value] of Object.entries(dict)) {
  if (!(value in newDict)) {
    tmp = [];
  } else {
    tmp = newDict[value];
  }
  tmp.push(key);
  newDict[value] = tmp;
}
console.log(newDict);
