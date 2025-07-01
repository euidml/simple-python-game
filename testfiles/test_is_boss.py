from unittest import TestCase
from game import is_boss


class Test(TestCase):
    def setUp(self) -> None:
        self.rows = 5
        self.columns = 5

    def test_is_boss_True(self):
        character = {"Location": {"X": 4, "Y": 4}}
        actual = is_boss(self.rows, self.columns, character)
        self.assertTrue(actual)

    def test_is_boss_False(self):
        character = {"Location": {"X": 3, "Y": 4}}
        actual = is_boss(self.rows, self.columns, character)
        self.assertFalse(actual)

    def test_is_boss_False_neg_nums(self):
        character = {"Location": {"X": -1, "Y": -1}}
        actual = is_boss(self.rows, self.columns, character)
        self.assertFalse(actual)

    def test_is_boss_False_neg_nums_and_zero_rows_and_columns(self):
        character = {"Location": {"X": -1, "Y": -1}}
        actual = is_boss(0, 0, character)
        self.assertTrue(actual)
