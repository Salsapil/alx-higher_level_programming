import unittest
from models.square import Square
from models.base import Base


class SquareTest(unittest.TestCase):

    def test_init(self):
        square = Square(1)
        self.assertEqual(square.width, 1)
        self.assertEqual(square.height, 1)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)


if __name__ == "__main__":
    unittest.main()
