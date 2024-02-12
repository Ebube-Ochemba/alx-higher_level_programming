#!/usr/bin/node
// A script that prints a square.

const num = Number(process.argv[2]);

if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let idx = 0; idx < num; idx++) {
    let row = '';
    for (let idy = 0; idy < num; idy++) {
      row += 'X';
    }
    console.log(row);
  }
}
