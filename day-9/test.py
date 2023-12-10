import unittest
import functools
from utils import *

class TestUtils(unittest.TestCase):
    def test_should_get_next_sequence(self):
        self.assertListEqual([1,1], getNextSequence([1,2,3]))
        self.assertListEqual([0, 0, 0], getNextSequence([1,1,1,1]))
        self.assertListEqual([6, 10, 16, 25], getNextSequence([3, 9 ,19, 35, 60]))
if __name__ == '__main__':
    unittest.main()