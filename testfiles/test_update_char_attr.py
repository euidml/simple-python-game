from unittest import TestCase
from game import update_char_attr


class Test(TestCase):

    def setUp(self) -> None:

        self.character_python_warrior_1 = {'Adding Level Up Attr Amount': {'Max Damage': 10, 'Max HP': 30,
                                                                           'Min Damage': 10},
                                           'Class': 'python warrior', 'Damage': {'Max Damage': 12, 'Min Damage': 9},
                                           'EXP': 0,
                                           'HP': 100, 'Level': 1,
                                           'Level Name': {'Level1': 'python soldier', 'Level2': 'python warrior',
                                                          'Level3': 'python hero'},
                                           'Location': {'X': 2, 'Y': 2}, 'Max HP': 100, 'Name': 'Edward',
                                           'Passive': 'pythonic'}
        self.character_web_dev_assassin_1 = {'Adding Level Up Attr Amount': {'Max Damage': 15,
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
        self.character_db_guardian_1 = {'Adding Level Up Attr Amount': {'Max Damage': 7,
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

        self.character_project_sorcerer_1 = {'Adding Level Up Attr Amount': {'Max Damage': 20,
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

        self.character_python_warrior_2 = {'Adding Level Up Attr Amount': {'Max Damage': 10,
                                                                           'Max HP': 30,
                                                                           'Min Damage': 10},
                                           'Class': 'python warrior',
                                           'Damage': {'Max Damage': 22, 'Min Damage': 19},
                                           'EXP': 10,
                                           'HP': 130,
                                           'Level': 2,
                                           'Level Name': {'Level1': 'python soldier',
                                                          'Level2': 'python warrior',
                                                          'Level3': 'python hero'},
                                           'Location': {'X': 2, 'Y': 2},
                                           'Max HP': 130,
                                           'Name': 'Edward',
                                           'Passive': 'pythonic'}

        self.character_web_dev_assassin_2 = {'Adding Level Up Attr Amount': {'Max Damage': 15,
                                                                             'Max HP': 15,
                                                                             'Min Damage': 5},
                                             'Class': 'web dev assassin',
                                             'Damage': {'Max Damage': 30, 'Min Damage': 10},
                                             'EXP': 10,
                                             'HP': 95,
                                             'Level': 2,
                                             'Level Name': {'Level1': 'html yegg',
                                                            'Level2': 'web dev assassin',
                                                            'Level3': 'react master'},
                                             'Location': {'X': 2, 'Y': 2},
                                             'Max HP': 95,
                                             'Name': 'Edward',
                                             'Passive': "employ's legend"}

        self.character_db_guardian_2 = {'Adding Level Up Attr Amount': {'Max Damage': 7,
                                                                        'Max HP': 30,
                                                                        'Min Damage': 5},
                                        'Class': 'db guardian',
                                        'Damage': {'Max Damage': 17, 'Min Damage': 10},
                                        'EXP': 10,
                                        'HP': 150,
                                        'Level': 2,
                                        'Level Name': {'Level1': 'query keeper',
                                                       'Level2': 'sql guardian',
                                                       'Level3': 'db guardian'},
                                        'Location': {'X': 2, 'Y': 2},
                                        'Max HP': 150,
                                        'Name': 'Edward',
                                        'Passive': 'security'}

        self.character_project_sorcerer_2 = {'Adding Level Up Attr Amount': {'Max Damage': 20,
                                                                             'Max HP': 10,
                                                                             'Min Damage': 5},
                                             'Class': 'project sorcerer',
                                             'Damage': {'Max Damage': 33, 'Min Damage': 10},
                                             'EXP': 10,
                                             'HP': 80,
                                             'Level': 2,
                                             'Level Name': {'Level1': 'project apprentice',
                                                            'Level2': 'project sorcerer',
                                                            'Level3': 'github magician'},
                                             'Location': {'X': 2, 'Y': 2},
                                             'Max HP': 80,
                                             'Name': 'Edward',
                                             'Passive': 'agile'}

    def test_update_char_attr_python_warrior_1(self):
        update_char_attr(self.character_python_warrior_1)
        actual = self.character_python_warrior_1
        expect = {'Adding Level Up Attr Amount': {'Max Damage': 10,
                                                  'Max HP': 30,
                                                  'Min Damage': 10},
                  'Class': 'python warrior',
                  'Damage': {'Max Damage': 22, 'Min Damage': 19},
                  'EXP': 0,
                  'HP': 130,
                  'Level': 2,
                  'Level Name': {'Level1': 'python soldier',
                                 'Level2': 'python warrior',
                                 'Level3': 'python hero'},
                  'Location': {'X': 2, 'Y': 2},
                  'Max HP': 130,
                  'Name': 'Edward',
                  'Passive': 'pythonic'}
        self.assertEqual(expect, actual)

    def test_update_char_attr_web_dev_assassin_1(self):
        update_char_attr(self.character_web_dev_assassin_1)
        actual = self.character_web_dev_assassin_1
        expect = {'Adding Level Up Attr Amount': {'Max Damage': 15,
                                                  'Max HP': 15,
                                                  'Min Damage': 5},
                  'Class': 'web dev assassin',
                  'Damage': {'Max Damage': 30, 'Min Damage': 10},
                  'EXP': 0,
                  'HP': 95,
                  'Level': 2,
                  'Level Name': {'Level1': 'html yegg',
                                 'Level2': 'web dev assassin',
                                 'Level3': 'react master'},
                  'Location': {'X': 2, 'Y': 2},
                  'Max HP': 95,
                  'Name': 'Edward',
                  'Passive': "employ's legend"}
        self.assertEqual(expect, actual)

    def test_update_character_db_guardian_1(self):
        update_char_attr(self.character_db_guardian_1)
        actual = self.character_db_guardian_1
        expect = {'Adding Level Up Attr Amount': {'Max Damage': 7,
                                                  'Max HP': 30,
                                                  'Min Damage': 5},
                  'Class': 'db guardian',
                  'Damage': {'Max Damage': 17, 'Min Damage': 10},
                  'EXP': 0,
                  'HP': 150,
                  'Level': 2,
                  'Level Name': {'Level1': 'query keeper',
                                 'Level2': 'sql guardian',
                                 'Level3': 'db guardian'},
                  'Location': {'X': 2, 'Y': 2},
                  'Max HP': 150,
                  'Name': 'Edward',
                  'Passive': 'security'}
        self.assertEqual(expect, actual)

    def test_update_character_project_sorcerer_1(self):
        update_char_attr(self.character_project_sorcerer_1)
        actual = self.character_project_sorcerer_1
        expect = {'Adding Level Up Attr Amount': {'Max Damage': 20,
                                                  'Max HP': 10,
                                                  'Min Damage': 5},
                  'Class': 'project sorcerer',
                  'Damage': {'Max Damage': 33, 'Min Damage': 10},
                  'EXP': 0,
                  'HP': 80,
                  'Level': 2,
                  'Level Name': {'Level1': 'project apprentice',
                                 'Level2': 'project sorcerer',
                                 'Level3': 'github magician'},
                  'Location': {'X': 2, 'Y': 2},
                  'Max HP': 80,
                  'Name': 'Edward',
                  'Passive': 'agile'}
        self.assertEqual(expect, actual)

    def test_update_character_python_warrior_2(self):
        update_char_attr(self.character_python_warrior_2)
        actual = self.character_python_warrior_2
        expect = {'Adding Level Up Attr Amount': {'Max Damage': 10,
                                                  'Max HP': 30,
                                                  'Min Damage': 10},
                  'Class': 'python warrior',
                  'Damage': {'Max Damage': 32, 'Min Damage': 29},
                  'EXP': 0,
                  'HP': 160,
                  'Level': 3,
                  'Level Name': {'Level1': 'python soldier',
                                 'Level2': 'python warrior',
                                 'Level3': 'python hero'},
                  'Location': {'X': 2, 'Y': 2},
                  'Max HP': 160,
                  'Name': 'Edward',
                  'Passive': 'pythonic'}
        self.assertEqual(expect, actual)

    def test_update_character_web_dev_assassin_2(self):
        update_char_attr(self.character_web_dev_assassin_2)
        actual = self.character_web_dev_assassin_2
        expect = {'Adding Level Up Attr Amount': {'Max Damage': 15,
                                                  'Max HP': 15,
                                                  'Min Damage': 5},
                  'Class': 'web dev assassin',
                  'Damage': {'Max Damage': 45, 'Min Damage': 15},
                  'EXP': 0,
                  'HP': 110,
                  'Level': 3,
                  'Level Name': {'Level1': 'html yegg',
                                 'Level2': 'web dev assassin',
                                 'Level3': 'react master'},
                  'Location': {'X': 2, 'Y': 2},
                  'Max HP': 110,
                  'Name': 'Edward',
                  'Passive': "employ's legend"}
        self.assertEqual(expect, actual)

    def test_update_character_db_guardian_2(self):
        update_char_attr(self.character_db_guardian_2)
        actual = self.character_db_guardian_2
        expect = {'Adding Level Up Attr Amount': {'Max Damage': 7,
                                                  'Max HP': 30,
                                                  'Min Damage': 5},
                  'Class': 'db guardian',
                  'Damage': {'Max Damage': 24, 'Min Damage': 15},
                  'EXP': 0,
                  'HP': 180,
                  'Level': 3,
                  'Level Name': {'Level1': 'query keeper',
                                 'Level2': 'sql guardian',
                                 'Level3': 'db guardian'},
                  'Location': {'X': 2, 'Y': 2},
                  'Max HP': 180,
                  'Name': 'Edward',
                  'Passive': 'security'}
        self.assertEqual(expect, actual)

    def test_update_character_project_sorcerer_2(self):
        update_char_attr(self.character_project_sorcerer_2)
        actual = self.character_project_sorcerer_2
        expect = {'Adding Level Up Attr Amount': {'Max Damage': 20,
                                                  'Max HP': 10,
                                                  'Min Damage': 5},
                  'Class': 'project sorcerer',
                  'Damage': {'Max Damage': 53, 'Min Damage': 15},
                  'EXP': 0,
                  'HP': 90,
                  'Level': 3,
                  'Level Name': {'Level1': 'project apprentice',
                                 'Level2': 'project sorcerer',
                                 'Level3': 'github magician'},
                  'Location': {'X': 2, 'Y': 2},
                  'Max HP': 90,
                  'Name': 'Edward',
                  'Passive': 'agile'}
        self.assertEqual(expect, actual)

    def test_update_character_update_attr_without_exp_10(self):
        self.character_project_sorcerer_1["EXP"] = 5
        update_char_attr(self.character_project_sorcerer_1)
        actual_attr = self.character_project_sorcerer_1
        expect_attr = {'Adding Level Up Attr Amount': {'Max Damage': 20,
                                                       'Max HP': 10,
                                                       'Min Damage': 5},
                       'Class': 'project sorcerer',
                       'Damage': {'Max Damage': 33, 'Min Damage': 10},
                       'EXP': 0,
                       'HP': 80,
                       'Level': 2,
                       'Level Name': {'Level1': 'project apprentice',
                                      'Level2': 'project sorcerer',
                                      'Level3': 'github magician'},
                       'Location': {'X': 2, 'Y': 2},
                       'Max HP': 80,
                       'Name': 'Edward',
                       'Passive': 'agile'}
        self.assertEqual(expect_attr, actual_attr)
