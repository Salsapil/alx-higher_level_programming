#!/usr/bin/node
exports.converter = function (base) {
  function convertNumber (num) {
    return num.toString(base);
  }
  return convertNumber;
};
