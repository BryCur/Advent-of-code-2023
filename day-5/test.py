import unittest
from utils import *

class TestUtils(unittest.TestCase):
        def test_shoud_generate_complete_seed_range(self):
            self.assertListEqual(
                [1,2,3,14,15,16,17,20,21,22,23,24,25,26,27,28,29], 
                parseSeedLine([1,3, 14,4, 20,10])
            )
if __name__ == '__main__':
    unittest.main()