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

    def test_should_sort_hand_properly(self):
        self.assertEqual(["2AAAA", "33332"], sorted(["33332", "2AAAA"], key=functools.cmp_to_key(compareSameStrengthHand)))
        self.assertEqual(["77788", "77888" ], sorted(["77888", "77788"], key=functools.cmp_to_key(compareSameStrengthHand)))
        self.assertEqual(["KTJJT", "KK677"], sorted(["KK677", "KTJJT"], key=functools.cmp_to_key(compareSameStrengthHand)))

    def test_should_give_best_hand_with_jokers(self): 
        #no jokers:
        self.assertEqual(Hand.HIGH_CARD, getJokeredHand("23456"))
        self.assertEqual(Hand.SINGLE_PAIR, getJokeredHand("A23A4"))
        self.assertEqual(Hand.DOUBLE_PAIR, getJokeredHand("23432"))
        self.assertEqual(Hand.THREE_OF_KIND, getJokeredHand("TTT98"))
        self.assertEqual(Hand.FULL_HOUSE, getJokeredHand("23332"))
        self.assertEqual(Hand.FOUR_OF_KIND, getJokeredHand("AA8AA"))
        self.assertEqual(Hand.FIVE_OF_KIND, getJokeredHand("AAAAA"))

        #jokers: 
        self.assertEqual(Hand.THREE_OF_KIND, getJokeredHand("2234J"))
        self.assertEqual(Hand.SINGLE_PAIR, getJokeredHand("2345J"))
        self.assertEqual(Hand.FULL_HOUSE, getJokeredHand("AAQQJ"))
        self.assertEqual(Hand.FOUR_OF_KIND, getJokeredHand("T55J5"))
        self.assertEqual(Hand.FOUR_OF_KIND, getJokeredHand("KTJJT"))
        self.assertEqual(Hand.FOUR_OF_KIND, getJokeredHand("QJJJA"))
        self.assertEqual(Hand.FIVE_OF_KIND, getJokeredHand("2222J"))

        self.assertEqual
if __name__ == '__main__':
    unittest.main()