#!/usr/bin/node
// A script that searches the second biggest integer in the list of arguments.

const myArgs = process.argv.slice(2);
function compare (a, b) {
  return a - b;
}

if (myArgs.length === 0 || myArgs.length < 2) {
  console.log(0);
} else {
  let myList = [];

  for (const arg in myArgs) {
    myList.push(Number(myArgs[arg]));
  }
  myList = myList.sort(compare);
  console.log(myList[myList.length - 2]);
}
