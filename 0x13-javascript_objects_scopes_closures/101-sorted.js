#!/usr/bin/node
const dict = require('./101-data.js').dict;
const dictionary = {};

for (const userId in dict) {
  const occurrence = dict[userId];
  dictionary[occurrence] = dictionary[occurrence] || [];
  dictionary[occurrence].push(userId);
}
console.log(dictionary);
