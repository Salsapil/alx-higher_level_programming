#!/usr/bin/node
const args = parseInt(process.argv[2]);
if (isNaN(args)) {
  console.log('Missing number of occurrences');
} else {
  for (let x = 0; x < args; x++) {
    console.log('C is fun');
  }
}
