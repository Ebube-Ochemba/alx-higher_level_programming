#!/usr/bin/node
// A script that prints x times "C is fun".

const num = Number(process.argv[2]);

if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  for (let idx = 0; idx < num; idx++) {
    console.log('C is fun');
  }
}
