#!/usr/bin/node

const { dict } = require('./101-data');

const newDict = {};

let tmp = [];
for (const [ID, occurrence] of Object.entries(dict)) {
  if (!(occurrence in newDict)) {
    tmp = [];
  } else {
    tmp = newDict[occurrence];
  }
  tmp.push(ID);
  newDict[occurrence] = tmp;
}
console.log(newDict);
