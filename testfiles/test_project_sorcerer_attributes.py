from unittest import TestCase
from game import project_sorcerer_attributes


class Test(TestCase):
    def test_project_sorcerer_attributes_valid(self):
        actual = project_sorcerer_attributes()
        expect = {"HP": 70, "Max HP": 70, "Passive": "agile", "Damage": {"Max Damage": 13, "Min Damage": 5},
                  "Level Name": {"Level1": "project apprentice", "Level2": "project sorcerer",
                                 "Level3": "github magician"},
                  "Adding Level Up Attr Amount": {"Max HP": 10, "Max Damage": 20, "Min Damage": 5}}
        self.assertEqual(expect, actual)

    def test_project_sorcerer_attributes_invalid_hp_Max_hp(self):
        actual = project_sorcerer_attributes()
        expect = {"HP": 60, "Max HP": 60, "Passive": "agile", "Damage": {"Max Damage": 13, "Min Damage": 5},
                  "Level Name": {"Level1": "project apprentice", "Level2": "project sorcerer",
                                 "Level3": "github magician"},
                  "Adding Level Up Attr Amount": {"Max HP": 10, "Max Damage": 20, "Min Damage": 5}}
        self.assertNotEqual(expect, actual)

    def test_project_sorcerer_attributes_invalid_passive(self):
        actual = project_sorcerer_attributes()
        expect = {"HP": 70, "Max HP": 70, "Passive": "SDLC", "Damage": {"Max Damage": 13, "Min Damage": 5},
                  "Level Name": {"Level1": "project apprentice", "Level2": "project sorcerer",
                                 "Level3": "github magician"},
                  "Adding Level Up Attr Amount": {"Max HP": 10, "Max Damage": 20, "Min Damage": 5}}
        self.assertNotEqual(expect, actual)

    def test_project_sorcerer_attributes_invalid_damage(self):
        actual = project_sorcerer_attributes()
        expect = {"HP": 70, "Max HP": 70, "Passive": "agile", "Damage": {"Max Damage": 10, "Min Damage": 7},
                  "Level Name": {"Level1": "project apprentice", "Level2": "project sorcerer",
                                 "Level3": "github magician"},
                  "Adding Level Up Attr Amount": {"Max HP": 10, "Max Damage": 20, "Min Damage": 5}}
        self.assertNotEqual(expect, actual)

    def test_project_sorcerer_attributes_invalid_Level_Name(self):
        actual = project_sorcerer_attributes()
        expect = {"HP": 70, "Max HP": 70, "Passive": "agile", "Damage": {"Max Damage": 13, "Min Damage": 5},
                  "Level Name": {"Level1": "project magician", "Level2": "project apprentice",
                                 "Level3": "github sorcerer"},
                  "Adding Level Up Attr Amount": {"Max HP": 10, "Max Damage": 20, "Min Damage": 5}}
        self.assertNotEqual(expect, actual)

    def test_project_sorcerer_attributes_invalid_Level_up_point(self):
        actual = project_sorcerer_attributes()
        expect = {"HP": 70, "Max HP": 70, "Passive": "agile", "Damage": {"Max Damage": 13, "Min Damage": 5},
                  "Level Name": {"Level1": "project apprentice", "Level2": "project sorcerer",
                                 "Level3": "github magician"},
                  "Adding Level Up Attr Amount": {"Max HP": 5, "Max Damage": 100, "Min Damage": -10}}
        self.assertNotEqual(expect, actual)
