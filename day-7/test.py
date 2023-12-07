import unittest
import functools
from utils import *

class TestUtils(unittest.TestCase):
    def test_should_identify_hands(self):
        self.assertEqual(Hand.HIGH_CARD, getHand("23456"))
        self.assertEqual(Hand.SINGLE_PAIR, getHand("A23A4"))
        self.assertEqual(Hand.DOUBLE_PAIR, getHand("23432"))
        self.assertEqual(Hand.THREE_OF_KIND, getHand("TTT98"))
        self.assertEqual(Hand.FULL_HOUSE, getHand("23332"))
        self.assertEqual(Hand.FOUR_OF_KIND, getHand("AA8AA"))
        self.assertEqual(Hand.FIVE_OF_KIND, getHand("AAAAA"))

    def tesT_should_sort_hand_properly(self):
        self.assertEqual(["33332", "2AAAA"], sorted(["2AAAA", "33332"], key=functools.cmp_to_key(compareSameStrengthHand)))
        self.assertEqual(["77888", "77788"], sorted(["77888", "77788"], key=functools.cmp_to_key(compareSameStrengthHand)))
        self.assertEqual(["KTJJT", "KK677"], sorted(["KK677", "KTJJT"], key=functools.cmp_to_key(compareSameStrengthHand)))


if __name__ == '__main__':
    unittest.main()