import unittest
from utils import *

class TestUtils(unittest.TestCase):
    pattern_column = [
        "#.##..##.",
        "..#.##.#.",
        "##......#",
        "##......#",
        "..#.##.#.",
        "..##..##.",
        "#.#.##.#."
    ]

    pattern_row = [
        "#...##..#",
        "#....#..#",
        "..##..###",
        "#####.##.",
        "#####.##.",
        "..##..###",
        "#....#..#"
    ]

    def test_should_find_pattern_in_rows(self): 
        self.assertEqual((1,6), find_row_mirror(self.pattern_row))
    
    def test_should_find_pattern_in_cols(self):
        self.assertEqual((1,8), find_col_mirror(self.pattern_column))

    def test_should_return_right_number_to_account(self):
        self.assertEqual(4, get_top_part_to_count((1,6)))
        self.assertEqual(5, get_top_part_to_count((1,8)))

if __name__ == '__main__':
    unittest.main()