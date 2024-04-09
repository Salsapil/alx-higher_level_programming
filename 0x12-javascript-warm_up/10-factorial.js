#!/usr/bin/node
function factorial (num) {
  if (isNaN(num)) {
    return 1;
  }
  if (num === 0) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

const n = parseInt(process.argv[2]);
console.log(factorial(n));
