#!/usr/bin/python3
for i in range(97, 123):
    if i == 112 or i == 101:
        continue
    print("{:c}".format(i), end="")