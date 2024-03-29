#!/usr/bin/python3
"""module for class"""


class BaseGeometry:
    """class"""
    def area(self):
        """calcuate area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """checks value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if type(name) is not str:
            raise Exception("{} must be a string".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
