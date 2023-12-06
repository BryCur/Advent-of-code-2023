import unittest
from utils import *

class TestUtils(unittest.TestCase):
        def test_should_return_minimum_time_to_win(self):
              self.assertEqual(2, getMinPushtimetoWin(7, 9))
              self.assertEqual(4, getMinPushtimetoWin(15, 40))
              self.assertEqual(11, getMinPushtimetoWin(30, 200))


        def test_should_return_minimum_time_to_win(self):
              self.assertEqual(5, getMaxPushtimetoWin(7, 9))
              self.assertEqual(11, getMaxPushtimetoWin(15, 40))
              self.assertEqual(19, getMaxPushtimetoWin(30, 200))


if __name__ == '__main__':
    unittest.main()