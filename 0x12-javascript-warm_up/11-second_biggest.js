#!/usr/bin/node
// A script that searches the second biggest integer in the list of arguments.

const argList = process.argv.slice;

if (argList.length <= 1) {
  console.log(0);
} else {
  let largest, secondLargest;

  for (const num in argList) {
    if (num > largest) {
      secondLargest = largest;
      largest = num;
    } else if (num > secondLargest && n !== largest) {
        secondLargest = n;
    }
  }
  console.log(secondLargest);
}
