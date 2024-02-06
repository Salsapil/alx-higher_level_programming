#!/usr/bin/python3
"""module"""


def write_file(filename="", text=""):
    """write file"""
    with open(filename,"w", encoding='UTF8') as file:
        return file.write(text)
