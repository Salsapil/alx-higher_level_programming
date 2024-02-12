#!/usr/bin/python3

"""
This module defines the `Rectangle` class
"""

from models.base import Base


class Rectangle(Base):
    """sub class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a new Rectangle object."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter for the width property.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width property.

        Args:
            value (int): The new width of the rectangle.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height property.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height property.

        Args:
            value (int): The new height of the rectangle.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Getter for the x-coordinate property.

        Returns:
            int: The x-coordinate of the rectangle.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for the x property.

        Args:
            value (int): The new x of the rectangle.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Getter for the y property.

        Returns:
            int: The y of the rectangle.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for the y-coordinate property.

        Args:
            value (int): The new y-coordinate of the rectangle.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """area of rectangle"""
        return self.width * self.height

    def display(self):
        """display special character"""
        print("\n" * self.y, end="")
        print(((" " * self.x) + "#" * self.width + "\n") * self.height, end="")

    def __str__(self):
        """"str"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} \
- {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """update dic"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """save to dic"""
        return {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'height': self.height,
            'width': self.width,
        }
