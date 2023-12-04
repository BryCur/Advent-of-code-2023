import unittest
from utils import *

class TestUtils(unittest.TestCase):
    test_matrix = [
        "12&....5",
        "......#.",
        ".....*..",
        ".....23.",
        "123.....",
        ".&2345..",
        "1.344..."
    ]

    def test_should_give_list_intersection(self):
        self.assertListEqual([], getListIntersection([1,2,3], [4,5,6]))
        self.assertListEqual([1,3,5], getListIntersection([1,3,5,7,8], [1,2,3,4,5]))

if __name__ == '__main__':
    unittest.main()