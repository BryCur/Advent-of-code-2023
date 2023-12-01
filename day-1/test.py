import unittest
from utils import *

class TestUtils(unittest.TestCase):

    def test_extract_digit_returns_a_list(self): 
        self.assertTrue(isinstance(exctractDigits(""), list))
        self.assertTrue(isinstance(exctractDigits("1two3fourasdfkj5"), list))
        self.assertTrue(isinstance(exctractDigits("asdfjkhalkj"), list))
        self.assertTrue(isinstance(exctractDigits("five8a3dsf4ssix"), list))

    def test_extract_all_numberical_digits(self): 
        self.assertListEqual([1,2,3], exctractDigits("1kjh2lkjh3lkjh"))

    def test_extract_digit_word_into_number(self): 
        self.assertListEqual([1,2,3], exctractDigits("oneasdftwoasdfthree"))

    def test_extract_numeric_values_and_word_in_order(self): 
        self.assertListEqual([1,4,2,3], exctractDigits("oneasd4ftwoasdfthree"))

    def test_compute_right_value_with_sequence(self):
        self.assertEquals(11, getValueFromSequence([1]))
        self.assertEquals(12, getValueFromSequence([1,2]))
        self.assertEquals(15, getValueFromSequence([1,3,4,5]))
        self.assertEquals(48, getValueFromSequence([4,5,1,6,8]))


if __name__ == '__main__':
    unittest.main()