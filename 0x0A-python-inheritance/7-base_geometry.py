#!/usr/bin/python3
"""module for class"""


class BaseGeometry:
    """class"""
    def area(self):
        """calcuate area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """checks value"""
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
