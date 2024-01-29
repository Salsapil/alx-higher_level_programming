#!/usr/bin/python3
"""Define Rectangle"""


class Rectangle:
    """Rectangle Class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Object of Class"""

        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """ print the rectangle with the character #

        Returns:
            join() is preferred over loops when you
                need to concatenate a large number of strings
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            return "\n".join([str(self.print_symbol) * self.width] *
                             self.height)

    def __repr__(self):
        """For developer"""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """For Delete"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Which is bigger"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """Class Method that use cls"""
        return Rectangle(size, size)
