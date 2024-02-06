#!/usr/bin/python3
"""module for a subclass"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


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


class Rectangle(BaseGeometry):
    """Rectangle subclass from BaseGeometry super class"""
    def __init__(self, width, height):
        """object"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
