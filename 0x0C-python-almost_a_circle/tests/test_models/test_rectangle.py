#!/usr/bin/python3
"""Base Class test cases"""
import unittest

from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_width(self):
        r = Rectangle(10, 7)

        self.assertEqual(r.width, 10)

        r.width = 5
        self.assertEqual(r.width, 5)

        with self.assertRaises(TypeError):
            r.width = "invalid"

        with self.assertRaises(ValueError):
            r.width = -1

    def test_height(self):
        r = Rectangle(10, 7)

        self.assertEqual(r.height, 7)

        r.height = 3
        self.assertEqual(r.height, 3)

        with self.assertRaises(TypeError):
            r.height = "invalid"

        with self.assertRaises(ValueError):
            r.height = -2

    def test_x(self):
        r = Rectangle(10, 7)

        self.assertEqual(r.x, 0)

        r.x = 2
        self.assertEqual(r.x, 2)

        with self.assertRaises(TypeError):
            r.x = "invalid"

        with self.assertRaises(ValueError):
            r.x = -1

    def test_y(self):
        r = Rectangle(10, 7)

        self.assertEqual(r.y, 0)

        r.y = 1
        self.assertEqual(r.y, 1)

        with self.assertRaises(TypeError):
            r.y = "invalid"

        with self.assertRaises(ValueError):
            r.y = -3

    def test_area(self):
        r = Rectangle(10, 7)
        self.assertEqual(r.area(), 70)

    def test_str(self):
        r = Rectangle(4, 6, 2, 1, 10)
        self.assertEqual(str(r), "[Rectangle] (10) 2/1 - 4/6")

    def test_update(self):
        r = Rectangle(10, 7)

        r.update(2, 5, 3, 1)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 1)


if __name__ == "__main__":
    unittest.main()
