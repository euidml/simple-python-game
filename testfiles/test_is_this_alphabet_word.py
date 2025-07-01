from unittest import TestCase
from game import is_this_alphabet_word


class Test(TestCase):

    def test_is_this_alphabet_edward(self):
        actual = is_this_alphabet_word("edward")
        self.assertTrue(actual)

    def test_is_this_alphabet_chris(self):
        actual = is_this_alphabet_word("chris")
        self.assertTrue(actual)

    def test_is_this_alphabet_empty(self):
        actual = is_this_alphabet_word("")
        self.assertTrue(actual)

    def test_is_this_alphabet_invalid_input(self):
        actual = is_this_alphabet_word("1")
        self.assertFalse(actual)
