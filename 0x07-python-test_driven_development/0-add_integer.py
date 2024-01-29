#!/usr/bin/python3
"""
module:
This is the first task
in Test-Driven-Development
"""


def add_integer(a, b=98):
    """ Adds 2 integers
    Args: a - integer number, b - integer number equal 98
    Return: sum of a and b """
    if type(a) not in [float, int]:
        raise TypeError("a must be an integer")
    if type(b) not in [float, int]:
        raise TypeError("b must be an integer")
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
