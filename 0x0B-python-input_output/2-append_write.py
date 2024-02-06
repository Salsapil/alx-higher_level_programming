#!/usr/bin/python3
"""module"""


def append_write(filename="", text=""):
    """write file"""
    with open(filename, "a", encoding='UTF8') as file:
        return file.write(text)
