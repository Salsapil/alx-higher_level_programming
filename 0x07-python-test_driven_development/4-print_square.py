#!/usr/bin/python3
"""
module:
This is the fourth task
in Test-Driven-Development
"""

def print_square(size):
    """Function
    Args:
        size: size
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
