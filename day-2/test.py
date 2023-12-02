import unittest
from utils import *

class TestUtils(unittest.TestCase):

    def test_should_return_game_id(self): 
        self.assertEqual(getGameId("sdafkjhasdf"), 0)
        self.assertEqual(getGameId("Game 1: aslkdjfhals"), 1)
        self.assertEqual(getGameId("Game 5: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"), 5)


    def test_sequence_should_be_a_list(self): 
        self.assertEqual(len(getSequence("asdlfjkb")), 1)
        self.assertEqual(len(getSequence("Game 1: aslkdjfhals")), 1)
        self.assertEqual(len(getSequence("Game 5: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")), 3)

    def test_should_identify_possible_sequence(self):
        possible_draft = "1 blue, 1 red, 1 green"
        max_possible_draft = f"{MAX_VALUES["blue"]} blue, {MAX_VALUES["red"]} red, {MAX_VALUES["green"]} green"
        impossible_draft_blue = f"{MAX_VALUES["blue"] +1} blue, 1 red, 1 green"
        impossible_draft_red = f"1 blue, {MAX_VALUES["red"] +1} red, 1 green"
        impossible_draft_green = f"1 blue, 1 red, {MAX_VALUES["green"]+1} green"

        self.assertTrue(isSequencePossible([possible_draft]))
        self.assertTrue(isSequencePossible([max_possible_draft]))
        self.assertFalse(isSequencePossible([impossible_draft_blue]))
        self.assertFalse(isSequencePossible([impossible_draft_red]))
        self.assertFalse(isSequencePossible([impossible_draft_green]))

        self.assertFalse(isSequencePossible([possible_draft, impossible_draft_green]))


        
    

if __name__ == '__main__':
    unittest.main()