from unittest import TestCase
from game import web_dev_assassin_attributes


class Test(TestCase):
    def test_web_dev_assassin_attributes_valid(self):
        actual = web_dev_assassin_attributes()
        expect = {"HP": 80, "Max HP": 80, "Passive": "employ's legend", "Damage": {"Max Damage": 15, "Min Damage": 5},
                  "Level Name": {"Level1": "html yegg", "Level2": "web dev assassin", "Level3": "react master"},
                  "Adding Level Up Attr Amount": {"Max HP": 15, "Max Damage": 15, "Min Damage": 5}}
        self.assertEqual(expect, actual)

    def test_web_dev_assassin_attributes_invalid_hp_Max_hp(self):
        actual = web_dev_assassin_attributes()
        expect = {"HP": 70, "Max HP": 70, "Passive": "employ's legend", "Damage": {"Max Damage": 15, "Min Damage": 5},
                  "Level Name": {"Level1": "html yegg", "Level2": "web dev assassin", "Level3": "react master"},
                  "Adding Level Up Attr Amount": {"Max HP": 15, "Max Damage": 15, "Min Damage": 5}}
        self.assertNotEqual(expect, actual)

    def test_web_dev_assassin_attributes_invalid_passive(self):
        actual = web_dev_assassin_attributes()
        expect = {"HP": 80, "Max HP": 80, "Passive": "1537", "Damage": {"Max Damage": 15, "Min Damage": 5},
                  "Level Name": {"Level1": "html yegg", "Level2": "web dev assassin", "Level3": "react master"},
                  "Adding Level Up Attr Amount": {"Max HP": 15, "Max Damage": 15, "Min Damage": 5}}
        self.assertNotEqual(expect, actual)

    def test_web_dev_assassin_attributes_invalid_damages(self):
        actual = web_dev_assassin_attributes()
        expect = {"HP": 80, "Max HP": 80, "Passive": "employ's legend", "Damage": {"Max Damage": -15, "Min Damage": 3},
                  "Level Name": {"Level1": "html yegg", "Level2": "web dev assassin", "Level3": "react master"},
                  "Adding Level Up Attr Amount": {"Max HP": 15, "Max Damage": 15, "Min Damage": 5}}
        self.assertNotEqual(expect, actual)

    def test_web_dev_assassin_attributes_invalid_Level_Name(self):
        actual = web_dev_assassin_attributes()
        expect = {"HP": 80, "Max HP": 80, "Passive": "employ's legend", "Damage": {"Max Damage": 15, "Min Damage": 5},
                  "Level Name": {"Level1": "react master", "Level2": "html yegg", "Level3": "web dev assassin"},
                  "Adding Level Up Attr Amount": {"Max HP": 15, "Max Damage": 15, "Min Damage": 5}}
        self.assertNotEqual(expect, actual)

    def test_web_dev_assassin_attributes_invalid_Level_up_point(self):
        actual = web_dev_assassin_attributes()
        expect = {"HP": 80, "Max HP": 80, "Passive": "employ's legend", "Damage": {"Max Damage": 15, "Min Damage": 5},
                  "Level Name": {"Level1": "react master", "Level2": "html yegg", "Level3": "web dev assassin"},
                  "Adding Level Up Attr Amount": {"Max HP": -10, "Max Damage": 10, "Min Damage": 7}}
        self.assertNotEqual(expect, actual)