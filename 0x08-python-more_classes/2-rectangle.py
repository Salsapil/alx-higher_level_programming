#!/usr/bin/python3
"""Define Rectangle"""


class Rectangle:
    """Rectangle Class"""

    def __init__(self, width=0, height=0):
        """Object of Class"""

        self.height = height
        self.width = width

    @property
    def width(self):
        """Property to retrieve
                Private instance attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Property Setter to set value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Property to retrieve
                Private instance attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Property Setter to set value"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of Rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of Rectangle"""
        if (self.__width == 0 or self.__height == 0):
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)
