from unittest import TestCase
from game import python_warrior_attributes


class Test(TestCase):
    def test_python_warrior_attributes_valid(self):
        actual = python_warrior_attributes()
        expect = {"HP": 100, "Max HP": 100, "Passive": "pythonic", "Damage": {"Max Damage": 12, "Min Damage": 9},
                  "Level Name": {"Level1": "python soldier", "Level2": "python warrior", "Level3": "python hero"},
                  "Adding Level Up Attr Amount": {"Max HP": 30, "Max Damage": 10, "Min Damage": 10}}
        self.assertEqual(expect, actual)

    def test_python_warrior_attributes_invalid_hp(self):
        actual = python_warrior_attributes()
        expect = {"HP": 90, "Max HP": 100, "Passive": "pythonic", "Damage": {"Max Damage": 12, "Min Damage": 9},
                  "Level Name": {"Level1": "python soldier", "Level2": "python warrior", "Level3": "python hero"},
                  "Adding Level Up Attr Amount": {"Max HP": 30, "Max Damage": 10, "Min Damage": 10}}
        self.assertNotEqual(expect, actual)

    def test_python_warrior_attributes_invalid_Max_hp(self):
        actual = python_warrior_attributes()
        expect = {"HP": 100, "Max HP": 110, "Passive": "pythonic", "Damage": {"Max Damage": 12, "Min Damage": 9},
                  "Level Name": {"Level1": "python soldier", "Level2": "python warrior", "Level3": "python hero"},
                  "Adding Level Up Attr Amount": {"Max HP": 30, "Max Damage": 10, "Min Damage": 10}}
        self.assertNotEqual(expect, actual)

    def test_python_warrior_attributes_invalid_Invalid_passive(self):
        actual = python_warrior_attributes()
        expect = {"HP": 100, "Max HP": 100, "Passive": "not_pythonic", "Damage": {"Max Damage": 12, "Min Damage": 9},
                  "Level Name": {"Level1": "python soldier", "Level2": "python warrior", "Level3": "python hero"},
                  "Adding Level Up Attr Amount": {"Max HP": 30, "Max Damage": 10, "Min Damage": 10}}
        self.assertNotEqual(expect, actual)

    def test_python_warrior_attributes_invalid_damages(self):
        actual = python_warrior_attributes()
        expect = {"HP": 100, "Max HP": 100, "Passive": "pythonic", "Damage": {"Max Damage": 100, "Min Damage": 0},
                  "Level Name": {"Level1": "python soldier", "Level2": "python warrior", "Level3": "python hero"},
                  "Adding Level Up Attr Amount": {"Max HP": 30, "Max Damage": 10, "Min Damage": 10}}
        self.assertNotEqual(expect, actual)

    def test_python_warrior_attributes_invalid_Level_names(self):
        actual = python_warrior_attributes()
        expect = {"HP": 100, "Max HP": 100, "Passive": "pythonic", "Damage": {"Max Damage": 12, "Min Damage": 9},
                  "Level Name": {"Level1": "python warrior", "Level2": "python hero", "Level3": "python soldier"},
                  "Adding Level Up Attr Amount": {"Max HP": 30, "Max Damage": 10, "Min Damage": 10}}
        self.assertNotEqual(expect, actual)

    def test_python_warrior_attributes_invalid_Level_up(self):
        actual = python_warrior_attributes()
        expect = {"HP": 100, "Max HP": 100, "Passive": "pythonic", "Damage": {"Max Damage": 12, "Min Damage": 9},
                  "Level Name": {"Level1": "python soldier", "Level2": "python warrior", "Level3": "python hero"},
                  "Adding Level Up Attr Amount": {"Max HP": - 30, "Max Damage": - 10, "Min Damage": 110}}
        self.assertNotEqual(expect, actual)