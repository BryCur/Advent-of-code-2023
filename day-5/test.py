import unittest
from utils import *

class TestUtils(unittest.TestCase):
    test_map = [
        "1 5 2",
        "20 60 20",
        "10 90 5"
    ]

    def test_should_give_list_intersection(self):
        self.assertListEqual([], getListIntersection([1,2,3], [4,5,6]))
        self.assertListEqual([1,3,5], getListIntersection([1,3,5,7,8], [1,2,3,4,5]))

if __name__ == '__main__':
    unittest.main()