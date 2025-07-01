from unittest import TestCase
from game import character_icon_generator


class Test(TestCase):

    def test_character_icon_generator_higher_than_80_percent(self):
        character = {"HP": 9, "Max HP": 10}
        actual = character_icon_generator(character)
        expect = "\U0001F601"
        self.assertEqual(expect, actual)

    def test_character_icon_generator_higher_than_50_percent(self):
        character = {"HP": 6, "Max HP": 10}
        actual = character_icon_generator(character)
        expect = "\U0001F642"
        self.assertEqual(expect, actual)

    def test_character_icon_generator_higher_than_25_percent(self):
        character = {"HP": 3, "Max HP": 10}
        actual = character_icon_generator(character)
        expect = "\U0001F613"
        self.assertEqual(expect, actual)

    def test_character_icon_generator_less_than_25_percent(self):
        character = {"HP": 1, "Max HP": 10}
        actual = character_icon_generator(character)
        expect = "\U0001F915"
        self.assertEqual(expect, actual)

    # those of tests below are impossible to happen, but not "invalid"
    def test_character_icon_generator_hp_0(self):
        character = {"HP": 0, "Max HP": 10}
        actual = character_icon_generator(character)
        expect = "\U0001F915"
        self.assertEqual(expect, actual)

    def test_character_icon_generator_over_100_percent(self):
        character = {"HP": 15, "Max HP": 10}
        actual = character_icon_generator(character)
        expect = "\U0001F601"
        self.assertEqual(expect, actual)