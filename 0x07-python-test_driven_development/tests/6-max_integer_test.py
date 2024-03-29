#!/usr/bin/python3
"""module"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class max(unittest.TestCase):

    def test_max_integer(self):
        """test max integer
        Args:
            self
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([4]), 4)
        self.assertEqual(max_integer([]), None)


if __name__ == "__main__":
    unittest.main
