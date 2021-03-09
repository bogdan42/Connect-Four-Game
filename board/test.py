import unittest
from board.BOARD import *

class MyTestCase(unittest.TestCase):
    def test_something(self):
        testboard = Board()
        assert type(testboard) == type(Board())


if __name__ == '__main__':
    unittest.main()
