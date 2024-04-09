#!/usr/bin/node
const args = process.argv.slice(2);
const intArgs = args.map(Number);
const sortedArgs = intArgs.sort((a, b) => b - a);

if (sortedArgs.length >= 2) {
  console.log(sortedArgs[1]);
} else {
  console.log(0);
}
