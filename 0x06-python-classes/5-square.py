#!/usr/bin/python3
"""square module"""


class Square:
    """define square"""

    def __init__(self, size=0):
        """Method in a class"""
        self.__size = size

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

    def area(self):
        """Public instance method
            return: current square area"""
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character"""
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="\n" if j is self.size - 1 and i != j else "")
        print()
