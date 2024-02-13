#!/usr/bin/python3
"""Base Class test cases"""
import unittest
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):

    def test_init(self):
        """Test Square initialization with valid arguments."""
        s1 = Square(5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertIsNotNone(s1.id)

        s2 = Square(7, 2, 3, 12)
        self.assertEqual(s2.width, 7)
        self.assertEqual(s2.height, 7)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 3)
        self.assertEqual(s2.id, 12)

    def test_str(self):
        """Test Square string representation."""
        s = Square(10)
        expected_str = f"[Square] ({s.id}) {s.x}/{s.y} - {s.width}"
        self.assertEqual(str(s), expected_str)

    def test_size_getter(self):
        """Test size getter property."""
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_size_setter(self):
        """Test size setter property."""
        s = Square(10)
        s.size = 20
        self.assertEqual(s.width, 20)
        self.assertEqual(s.height, 20)

    def test_to_dictionary(self):
        """Test Square to_dictionary method."""
        s = Square(5)
        expected_dict = {'id': s.id, 'x': s.x, 'size': s.size, 'y': s.y}
        self.assertEqual(s.to_dictionary(), expected_dict)


if __name__ == "__main__":
    unittest.main()
