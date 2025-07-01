from unittest import TestCase
from game import is_character_level_3


class Test(TestCase):

    def setUp(self) -> None:
        self.character = {}

    def test_is_character_level_3_level_1(self):
        self.character["Level"] = 1
        actual = is_character_level_3(self.character)
        self.assertFalse(actual)

    def test_is_character_level_3_level_2(self):
        self.character["Level"] = 2
        actual = is_character_level_3(self.character)
        self.assertFalse(actual)

    def test_is_character_level_3_level_3(self):
        self.character["Level"] = 3
        actual = is_character_level_3(self.character)
        self.assertTrue(actual)

    def test_is_character_level_3_level_neg_1(self):
        self.character["Level"] = - 1
        actual = is_character_level_3(self.character)
        self.assertFalse(actual)

    def test_is_character_level_3_level_4(self):
        self.character["Level"] = 4
        actual = is_character_level_3(self.character)
        self.assertFalse(actual)
