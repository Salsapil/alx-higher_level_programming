#!/usr/bin/node
const list = require('./100-data.js').list;
console.log(list);
const squaredList = [];
for (let i = 0; i < list.length; i++) {
  squaredList.push(list[i] * i);
}
console.log(squaredList);
