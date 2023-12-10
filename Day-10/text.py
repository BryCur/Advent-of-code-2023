import unittest
import functools
from utils import *

class TestUtils(unittest.TestCase):
    test_map = [
        "-L|F7",
        "7S-7|",
        "L|7||",
        "-L-J|",
        "L|-JF"
    ]

    test_map_2 = [
        "-7|F7",
        "FS-7|",
        "L|7||",
        "-L-J|",
        "L|-JF"
    ]

    def test_should_find_start(self): 
        self.assertTupleEqual((1,1), findStartingPos(self.test_map, "S"))

    def test_should_identify_starting_pipe_shape(self):
        self.assertSetEqual(set(["F"]), getStartingPipePossibleShape(self.test_map, (1,1)))
        self.assertSetEqual(set(["F", "J", "L", "|", "-", "7"]), getStartingPipePossibleShape(self.test_map_2, (1,1)))
        
if __name__ == '__main__':
    unittest.main()