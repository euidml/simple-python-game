from unittest import TestCase
from game import validate_move


class Test(TestCase):

    def setUp(self) -> None:
        self.character = {"Location": {"X": 0, "Y": 0}}
        self.rows = self.columns = 3

    def test_validate_move_valid_move_1(self):
        direction = (1, 0)
        actual = validate_move(self.character, direction, self.rows, self.columns)
        self.assertTrue(actual)

    def test_validate_move_valid_move_2(self):
        direction = (0, 1)
        actual = validate_move(self.character, direction, self.rows, self.columns)
        self.assertTrue(actual)

    def test_validate_move_invalid_move_1(self):
        direction = (-1, 0)
        actual = validate_move(self.character, direction, self.rows, self.columns)
        self.assertFalse(actual)

    def test_validate_move_invalid_move_2(self):
        direction = (0, -1)
        actual = validate_move(self.character, direction, self.rows, self.columns)
        self.assertFalse(actual)

    def test_validate_move_invalid_move_3(self):
        self.character["Location"]["X"] = self.character["Location"]["Y"] = 2
        direction = (1, 0)
        actual = validate_move(self.character, direction, self.rows, self.columns)
        self.assertFalse(actual)

    def test_validate_move_invalid_move_4(self):
        self.character["Location"]["X"] = self.character["Location"]["Y"] = 2
        direction = (0, 1)
        actual = validate_move(self.character, direction, self.rows, self.columns)
        self.assertFalse(actual)

    # tests invalid tuples
    def test_validate_move_nowhere(self):
        self.character["Location"]["X"] = self.character["Location"]["Y"] = 1
        direction = (0, 0)
        actual = validate_move(self.character, direction, self.rows, self.columns)
        self.assertTrue(actual)

    def test_validate_move_invalid_tuple_1(self):
        self.character["Location"]["X"] = self.character["Location"]["Y"] = 1
        direction = (0, 0)
        actual = validate_move(self.character, direction, self.rows, self.columns)
        self.assertTrue(actual)

    def test_validate_move_invalid_tuple_2(self):
        self.character["Location"]["X"] = self.character["Location"]["Y"] = 1
        direction = (1, 1)
        actual = validate_move(self.character, direction, self.rows, self.columns)
        self.assertTrue(actual)