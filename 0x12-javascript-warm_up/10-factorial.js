#!/usr/bin/node
const n = parseInt(process.argv[2]);
function factorial (Number) {
  if (isNaN(Number) || Number <= 1) {
    return 1;
  } else {
    return Number * factorial(Number - 1);
  }
}
console.log(factorial(n));
