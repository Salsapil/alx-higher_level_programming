#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

# result_add = add(10, 5)
# print("10 + 5 = {}".format(result_add))
# result_sub = sub(10, 5)
# print("10 - 5 = {}".format(result_sub))
# result_mul = mul(10, 5)
# print("10 * 5 = {}".format(result_mul))
# result_div = div(10, 5)
# print("10 / 5 = {}".format(result_div))

a = 10
b = 5
print(a, "+", b, "=", add(a, b))
print(a, "-", b, "=", sub(a, b))
print(a, "*", b, "=", mul(a, b))
print(a, "/", b, "=", div(a, b))
