import unittest
from utils import *

class TestUtils(unittest.TestCase):
    possible_draft = "1 blue, 1 red, 1 green"
    max_possible_draft = f"{MAX_VALUES["blue"]} blue, {MAX_VALUES["red"]} red, {MAX_VALUES["green"]} green"
    impossible_draft_blue = f"{MAX_VALUES["blue"] +1} blue, 1 red, 1 green"
    impossible_draft_red = f"1 blue, {MAX_VALUES["red"] +1} red, 1 green"
    impossible_draft_green = f"1 blue, 1 red, {MAX_VALUES["green"]+1} green"

    def test_should_return_game_id(self): 
        self.assertEqual(getGameId("sdafkjhasdf"), 0)
        self.assertEqual(getGameId("Game 1: aslkdjfhals"), 1)
        self.assertEqual(getGameId("Game 5: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"), 5)


    def test_sequence_should_be_a_list(self): 
        self.assertEqual(len(getSequence("asdlfjkb")), 1)
        self.assertEqual(len(getSequence("Game 1: aslkdjfhals")), 1)
        self.assertEqual(len(getSequence("Game 5: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")), 3)

    def test_should_identify_possible_sequence(self):


        self.assertTrue(isSequencePossible([self.possible_draft]))
        self.assertTrue(isSequencePossible([self.max_possible_draft]))
        self.assertFalse(isSequencePossible([self.impossible_draft_blue]))
        self.assertFalse(isSequencePossible([self.impossible_draft_red]))
        self.assertFalse(isSequencePossible([self.impossible_draft_green]))

        self.assertFalse(isSequencePossible([self.possible_draft, self.impossible_draft_green]))


    def test_should_return_minimum_set_of_dice_required(self):
        expected_result = {
            "blue": 1,
            "red": 1,
            "green": 1
        }
        self.assertDictEqual(getMinDiceRequired([self.possible_draft]), expected_result)

        expected_result = {
            "blue": 1,
            "red": MAX_VALUES["red"]+1,
            "green": 1
        }
        self.assertDictEqual(getMinDiceRequired([self.possible_draft, self.impossible_draft_red]), expected_result)
        
    

if __name__ == '__main__':
    unittest.main()