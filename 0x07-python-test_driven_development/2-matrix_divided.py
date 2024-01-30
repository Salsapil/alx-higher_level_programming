#!/usr/bin/python3
"""
module:
This is the second task 
in Test-Driven-Development
"""

def matrix_divided(matrix, div):
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
