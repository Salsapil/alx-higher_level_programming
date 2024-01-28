#!/usr/bin/python3
"""square module"""


class Square:
    """define square"""

    def __init__(self, size=0, position=(0, 0)):
        """Method in a class"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Public instance method
            return: current square area"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Public instance method
            return: current square area"""
        return self.__position

    @position.setter
    def position(self, value):
        if len(value) != 2 or not isinstance(value, tuple) or \
            not isinstance(value[0], int) or \
            not isinstance(value[1], int) or \
                value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Public instance method
            return: current square area"""
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
            for i in range(self.__position[1]):
                print()
