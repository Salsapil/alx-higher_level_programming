#!/usr/bin/python3
"""module for a subclass"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle subclass from BaseGeometry super class"""
    def __init__(self, width, height):
        """object"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """return area"""
        return self.__width * self.__height

    def __str__(self):
        """string"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
