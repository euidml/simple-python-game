from unittest import TestCase
from game import check_level_up


class Test(TestCase):

    def setUp(self) -> None:
        self.character = {"EXP": 5, "Level": 1}

    def test_check_level_up_false_to_2(self):
        actual = check_level_up(self.character)
        self.assertFalse(actual)

    def test_check_level_up_false_to_3(self):
        self.character["Level"] = 2
        actual = check_level_up(self.character)
        self.assertFalse(actual)

    def test_check_level_up_true_to_2(self):
        self.character["EXP"] = 10
        actual = check_level_up(self.character)
        self.assertTrue(actual)

    def test_check_level_up_true_to_e(self):
        self.character["EXP"], self.character["Level"] = 10, 2
        actual = check_level_up(self.character)
        self.assertTrue(actual)

    def test_check_level_up_false_at_3(self):
        self.character["EXP"], self.character["Level"] = 10, 3
        actual = check_level_up(self.character)
        self.assertFalse(actual)

    def test_check_level_up_false_at_0(self):
        self.character["EXP"], self.character["Level"] = 10, 0
        actual = check_level_up(self.character)
        self.assertFalse(actual)

    def test_check_level_up_false_at_neg(self):
        self.character["EXP"], self.character["Level"] = 10, -1
        actual = check_level_up(self.character)
        self.assertFalse(actual)