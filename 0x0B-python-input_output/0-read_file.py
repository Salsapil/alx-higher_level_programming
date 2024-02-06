#!/usr/bin/python3
"""module"""


def read_file(filename=""):
    """read file"""
    with open(filename, encoding='UTF8') as file:
        print(file.read(), end="")
