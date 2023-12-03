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

    def test_supported_symboles(self):
        should_all_pass = "+\"*%&/()=?!@#'^"
        should_all_fail = ". 1234567890qwertzuzuiopasdfghjklyxcvbnm"

        for char in should_all_fail:
            self.assertFalse(isCharSupportedSymbole(char))

        for char in should_all_pass:
            self.assertTrue(isCharSupportedSymbole(char))

    def test_extract_digit_returns_a_list(self): 
        self.assertEqual((0,2),findNextSupportedSymbolInMatrix(self.test_matrix, 0,0))
        self.assertEqual((1,6),findNextSupportedSymbolInMatrix(self.test_matrix, 0,3))
        self.assertEqual((2,5),findNextSupportedSymbolInMatrix(self.test_matrix, 1,7))
        self.assertEqual((5, 1), findNextSupportedSymbolInMatrix(self.test_matrix, 3,0))
        self.assertEqual((-1,-1), findNextSupportedSymbolInMatrix(self.test_matrix, 5,2))

    def test_should_give_all_number_position_from_center(self): 
        self.assertListEqual([(0,1)], getAdjacentNumberPositionsFrom(self.test_matrix, 0,2))
        self.assertListEqual([(3,5), (3,6)], getAdjacentNumberPositionsFrom(self.test_matrix, 2,6))

    def test_should_return_whole_number_on_position(self):
        self.assertEqual(12, consumeAndReturnNumberAtPosition(self.test_matrix, 0, 1))

    def test_should_not_read_same_number_twice_when_asked_from_different_positions(self):
        copy_of_test_matrix = self.test_matrix.copy()
        self.assertEqual(23, consumeAndReturnNumberAtPosition(copy_of_test_matrix, 3, 5))
        self.assertEqual(0, consumeAndReturnNumberAtPosition(copy_of_test_matrix, 3, 6))

    def test_should_count_all_number_around_position(self):
        self.assertEqual(1, countAllUniqueNumberAroundPos(self.test_matrix, 0, 2))
        self.assertEqual(4, countAllUniqueNumberAroundPos(self.test_matrix, 5, 1))

if __name__ == '__main__':
    unittest.main()