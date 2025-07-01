from unittest import TestCase
from game import db_guardian_attributes


class Test(TestCase):
    def test_db_guardian_attributes_valid(self):
        actual = db_guardian_attributes()
        expect = {"HP": 120, "Max HP": 120, "Passive": "security", "Damage": {"Max Damage": 10, "Min Damage": 5},
                  "Level Name": {"Level1": "query keeper", "Level2": "sql guardian", "Level3": "db guardian"},
                  "Adding Level Up Attr Amount": {"Max HP": 30, "Max Damage": 7, "Min Damage": 5}}
        self.assertEqual(expect, actual)

    def test_db_guardian_attributes_invalid_hp_max_hp(self):
        actual = db_guardian_attributes()
        expect = {"HP": 100, "Max HP": 100, "Passive": "security", "Damage": {"Max Damage": 10, "Min Damage": 5},
                  "Level Name": {"Level1": "query keeper", "Level2": "sql guardian", "Level3": "db guardian"},
                  "Adding Level Up Attr Amount": {"Max HP": 30, "Max Damage": 7, "Min Damage": 5}}
        self.assertNotEqual(expect, actual)

    def test_db_guardian_attributes_invalid_passive(self):
        actual = db_guardian_attributes()
        expect = {"HP": 120, "Max HP": 120, "Passive": "hacker", "Damage": {"Max Damage": 10, "Min Damage": 5},
                  "Level Name": {"Level1": "query keeper", "Level2": "sql guardian", "Level3": "db guardian"},
                  "Adding Level Up Attr Amount": {"Max HP": 30, "Max Damage": 7, "Min Damage": 5}}
        self.assertNotEqual(expect, actual)

    def test_db_guardian_attributes_invalid_damages(self):
        actual = db_guardian_attributes()
        expect = {"HP": 120, "Max HP": 120, "Passive": "security", "Damage": {"Max Damage": 100, "Min Damage": 50},
                  "Level Name": {"Level1": "query keeper", "Level2": "sql guardian", "Level3": "db guardian"},
                  "Adding Level Up Attr Amount": {"Max HP": 30, "Max Damage": 7, "Min Damage": 5}}
        self.assertNotEqual(expect, actual)

    def test_db_guardian_attributes_invalid_Level_Names(self):
        actual = db_guardian_attributes()
        expect = {"HP": 120, "Max HP": 120, "Passive": "security", "Damage": {"Max Damage": 10, "Min Damage": 5},
                  "Level Name": {"Level1": "db guardian", "Level2": "query keeper", "Level3": "sql guardian"},
                  "Adding Level Up Attr Amount": {"Max HP": 30, "Max Damage": 7, "Min Damage": 5}}
        self.assertNotEqual(expect, actual)

    def test_db_guardian_attributes_invalid_Level_up_points(self):
        actual = db_guardian_attributes()
        expect = {"HP": 120, "Max HP": 120, "Passive": "security", "Damage": {"Max Damage": 10, "Min Damage": 5},
                  "Level Name": {"Level1": "query keeper", "Level2": "sql guardian", "Level3": "db guardian"},
                  "Adding Level Up Attr Amount": {"Max HP": - 30, "Max Damage": 70, "Min Damage": 35}}
        self.assertNotEqual(expect, actual)