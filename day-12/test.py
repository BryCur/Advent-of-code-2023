import unittest
from utils import *

class TestUtils(unittest.TestCase):
    def test_should_separate_spring_sequence_from_numbers(self): 
        sequence, numbers = process_line(".??..??...?##. 1,1,3")
        self.assertEqual(".??..??...?##.", sequence)
        self.assertListEqual([1,1,3], numbers)
    
if __name__ == '__main__':
    unittest.main()