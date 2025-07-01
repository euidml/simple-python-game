from unittest import TestCase
from game import generate_character_attributes


class Test(TestCase):

    def test_generate_character_attributes_all_valid_cases_python_warrior(self):
        actual = generate_character_attributes("Edward", "python warrior", 5, 5)
        expect = {'Adding Level Up Attr Amount': {'Max Damage': 10,
                                                  'Max HP': 30,
                                                  'Min Damage': 10},
                  'Class': 'python warrior',
                  'Damage': {'Max Damage': 12, 'Min Damage': 9},
                  'EXP': 0,
                  'HP': 100,
                  'Level': 1,
                  'Level Name': {'Level1': 'python soldier',
                                 'Level2': 'python warrior',
                                 'Level3': 'python hero'},
                  'Location': {'X': 2, 'Y': 2},
                  'Max HP': 100,
                  'Name': 'Edward',
                  'Passive': 'pythonic'}
        self.assertEqual(expect, actual)

    def test_generate_character_attributes_all_valid_cases_web_dev_assassin(self):
        actual = generate_character_attributes("Edward", "web dev assassin", 5, 5)
        expect = {'Adding Level Up Attr Amount': {'Max Damage': 15,
                                                  'Max HP': 15,
                                                  'Min Damage': 5},
                  'Class': 'web dev assassin',
                  'Damage': {'Max Damage': 15, 'Min Damage': 5},
                  'EXP': 0,
                  'HP': 80,
                  'Level': 1,
                  'Level Name': {'Level1': 'html yegg',
                                 'Level2': 'web dev assassin',
                                 'Level3': 'react master'},
                  'Location': {'X': 2, 'Y': 2},
                  'Max HP': 80,
                  'Name': 'Edward',
                  'Passive': "employ's legend"}
        self.assertEqual(expect, actual)

    def test_generate_character_attributes_all_valid_cases_db_guardian(self):
        actual = generate_character_attributes("Edward", "db guardian", 5, 5)
        expect = {'Adding Level Up Attr Amount': {'Max Damage': 7,
                                                  'Max HP': 30,
                                                  'Min Damage': 5},
                  'Class': 'db guardian',
                  'Damage': {'Max Damage': 10, 'Min Damage': 5},
                  'EXP': 0,
                  'HP': 120,
                  'Level': 1,
                  'Level Name': {'Level1': 'query keeper',
                                 'Level2': 'sql guardian',
                                 'Level3': 'db guardian'},
                  'Location': {'X': 2, 'Y': 2},
                  'Max HP': 120,
                  'Name': 'Edward',
                  'Passive': 'security'}
        self.assertEqual(expect, actual)

    def test_generate_character_attributes_all_valid_cases_project_sorcerer(self):
        actual = generate_character_attributes("Edward", "project sorcerer", 5, 5)
        expect = {'Adding Level Up Attr Amount': {'Max Damage': 20,
                                                   'Max HP': 10,
                                                   'Min Damage': 5},
                   'Class': 'project sorcerer',
                   'Damage': {'Max Damage': 13, 'Min Damage': 5},
                   'EXP': 0,
                   'HP': 70,
                   'Level': 1,
                   'Level Name': {'Level1': 'project apprentice',
                                  'Level2': 'project sorcerer',
                                  'Level3': 'github magician'},
                   'Location': {'X': 2, 'Y': 2},
                   'Max HP': 70,
                   'Name': 'Edward',
                   'Passive': 'agile'}
        self.assertEqual(expect, actual)

    def test_generate_character_attributes_invalid_class_name(self):
        with self.assertRaises(KeyError):
            generate_character_attributes("Edward", "1510 hero", 5, 5)

    # this is to see what happens if I throw an empty string, this invalid case gets accepted in this test,
    # but it is going to get filtered by get_name() in the actual process
    def test_generate_character_attributes_invalid_name(self):
        actual = generate_character_attributes("", "project sorcerer", 5, 5)
        expect = {'Adding Level Up Attr Amount': {'Max Damage': 20,
                                                   'Max HP': 10,
                                                   'Min Damage': 5},
                   'Class': 'project sorcerer',
                   'Damage': {'Max Damage': 13, 'Min Damage': 5},
                   'EXP': 0,
                   'HP': 70,
                   'Level': 1,
                   'Level Name': {'Level1': 'project apprentice',
                                  'Level2': 'project sorcerer',
                                  'Level3': 'github magician'},
                   'Location': {'X': 2, 'Y': 2},
                   'Max HP': 70,
                   'Name': '',
                   'Passive': 'agile'}
        self.assertEqual(expect, actual)

    def test_generate_character_attributes_negative_rows_and_columns(self):
        rows = columns = - 5
        actual = generate_character_attributes("Edward", "project sorcerer", rows, columns)
        expect = {'Adding Level Up Attr Amount': {'Max Damage': 20,
                                                   'Max HP': 10,
                                                   'Min Damage': 5},
                   'Class': 'project sorcerer',
                   'Damage': {'Max Damage': 13, 'Min Damage': 5},
                   'EXP': 0,
                   'HP': 70,
                   'Level': 1,
                   'Level Name': {'Level1': 'project apprentice',
                                  'Level2': 'project sorcerer',
                                  'Level3': 'github magician'},
                   'Location': {'X': - 3, 'Y': - 3},
                   'Max HP': 70,
                   'Name': 'Edward',
                   'Passive': 'agile'}
        self.assertEqual(expect, actual)
