from unittest import TestCase
from game import class_attributes


class Test(TestCase):
    def test_class_attributes_input_python_warrior(self):
        actual = class_attributes("python warrior")
        expect = {'Adding Level Up Attr Amount': {'Max Damage': 10,
                                                  'Max HP': 30,
                                                  'Min Damage': 10},
                  'Damage': {'Max Damage': 12, 'Min Damage': 9},
                  'HP': 100,
                  'Level Name': {'Level1': 'python soldier',
                                 'Level2': 'python warrior',
                                 'Level3': 'python hero'},
                  'Max HP': 100,
                  'Passive': 'pythonic'}
        self.assertEqual(expect, actual)

    def test_class_attributes_input_web_dev_assassin(self):
        actual = class_attributes("web dev assassin")
        expect = {'Adding Level Up Attr Amount': {'Max Damage': 15,
                                                  'Max HP': 15,
                                                  'Min Damage': 5},
                  'Damage': {'Max Damage': 15, 'Min Damage': 5},
                  'HP': 80,
                  'Level Name': {'Level1': 'html yegg',
                                 'Level2': 'web dev assassin',
                                 'Level3': 'react master'},
                  'Max HP': 80,
                  'Passive': "employ's legend"}
        self.assertEqual(expect, actual)

    def test_class_attributes_input_db_guardian(self):
        actual = class_attributes("db guardian")
        expect = {'Adding Level Up Attr Amount': {'Max Damage': 7,
                                                  'Max HP': 30,
                                                  'Min Damage': 5},
                  'Damage': {'Max Damage': 10, 'Min Damage': 5},
                  'HP': 120,
                  'Level Name': {'Level1': 'query keeper',
                                 'Level2': 'sql guardian',
                                 'Level3': 'db guardian'},
                  'Max HP': 120,
                  'Passive': 'security'}
        self.assertEqual(expect, actual)

    def test_class_attributes_input_project_sorcerer(self):
        actual = class_attributes("project sorcerer")
        expect = {'Adding Level Up Attr Amount': {'Max Damage': 20,
                                                  'Max HP': 10,
                                                  'Min Damage': 5},
                  'Damage': {'Max Damage': 13, 'Min Damage': 5},
                  'HP': 70,
                  'Level Name': {'Level1': 'project apprentice',
                                 'Level2': 'project sorcerer',
                                 'Level3': 'github magician'},
                  'Max HP': 70,
                  'Passive': 'agile'}
        self.assertEqual(expect, actual)

    def test_class_attributes_input_raise_Keyerror_1(self):
        with self.assertRaises(KeyError):
            class_attributes("")

    def test_class_attributes_input_raise_Keyerror_2(self):
        with self.assertRaises(KeyError):
            class_attributes("1510 lover")

    def test_class_attributes_input_raise_Keyerror_3(self):
        with self.assertRaises(KeyError):
            class_attributes("python_warrior")