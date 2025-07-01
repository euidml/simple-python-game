from unittest import TestCase
from unittest.mock import patch
from game import generate_character


class Test(TestCase):

    def setUp(self) -> None:
        self.columns = self.rows = 5

    @patch('game.get_class', return_value="python warrior")
    @patch('game.get_name', return_value="Edward")
    def test_generate_character_python_warrior(self, mock_name, mock_class):
        expect = {'Adding Level Up Attr Amount': {'Max Damage': 10, 'Max HP': 30, 'Min Damage': 10},
                  "Class": 'python warrior',
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
        actual = generate_character(columns=self.columns, rows=self.rows)
        self.assertEqual(expect, actual)

    @patch('game.get_class', return_value="web dev assassin")
    @patch('game.get_name', return_value="Edward")
    def test_generate_character_web_dev_assassin(self, mock_name, mock_class):
        expect = {"Adding Level Up Attr Amount": {'Max Damage': 15,
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
        actual = generate_character(columns=self.columns, rows=self.rows)
        self.assertEqual(expect, actual)

    @patch('game.get_class', return_value="db guardian")
    @patch('game.get_name', return_value="Edward")
    def test_generate_character_db_guardian(self, mock_name, mock_class):
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
        actual = generate_character(columns=self.columns, rows=self.rows)
        self.assertEqual(expect, actual)

    @patch('game.get_class', return_value="project sorcerer")
    @patch('game.get_name', return_value="Edward")
    def test_generate_character_project_sorcerer(self, mock_name, mock_class):
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
        actual = generate_character(columns=self.columns, rows=self.rows)
        self.assertEqual(expect, actual)

    @patch('game.get_class', return_value="global object")
    @patch('game.get_name', return_value="Edward")
    def test_generate_character_raising_error_class(self, mock_name, mock_class):
        with self.assertRaises(KeyError):
            generate_character(columns=self.columns, rows=self.rows)

    @patch('game.get_class', return_value="python warrior")
    @patch('game.get_name', return_value="")
    def test_generate_character_raising_error_name(self, mock_name, mock_class):
        with self.assertRaises(ValueError):
            generate_character(columns=self.columns, rows=self.rows)
            raise ValueError
