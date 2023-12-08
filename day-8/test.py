import unittest
import functools
from utils import *

class TestUtils(unittest.TestCase):
    def test_parsing_input_to_tuple(self):
        self.assertTupleEqual(("BBB", "BBB"), process_input_tuple("(BBB, BBB)"))
if __name__ == '__main__':
    unittest.main()