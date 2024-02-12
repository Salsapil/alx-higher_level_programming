#!/usr/bin/python3

"""module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """sub class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str"""
        return f"[Square] ({self.id}) {self.x}/{self.y} \
- {self.width}"

    @property
    def size(self):
        """
        getter for size property

        Returns:
            int: The size of the rectangle.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        setter for size property

        Args:
            value (int): The new size of the rectangle.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update dict"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """save to dict"""
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
