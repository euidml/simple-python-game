from unittest import TestCase
from unittest.mock import patch
from game import norm_monster_generator


class Test(TestCase):
    def setUp(self) -> None:
        self.character = {"Level": 1}

    @patch('random.randint', return_value=0)
    def test_norm_monster_generator_Algorithm(self, mock_random_num):
        actual = norm_monster_generator(self.character)
        expect = {'Damage': {'Max Damage': 4, 'Min Damage': 3},
                  'EXP': 4,
                  'HP': 20,
                  'Is Boss': False,
                  'Name': 'Algorithm',
                  'Passive': None}
        self.assertEqual(expect, actual)

    @patch('random.randint', return_value=1)
    def test_norm_monster_generator_DataStructure(self, mock_random_num):
        actual = norm_monster_generator(self.character)
        expect = {'Damage': {'Max Damage': 7, 'Min Damage': 2},
                  'EXP': 4,
                  'HP': 15,
                  'Is Boss': False,
                  'Name': 'DataStructure',
                  'Passive': None}
        self.assertEqual(expect, actual)

    @patch('random.randint', return_value=2)
    def test_norm_monster_generator_DB(self, mock_random_num):
        actual = norm_monster_generator(self.character)
        expect = {'Damage': {'Max Damage': 30, 'Min Damage': 1},
                  'EXP': 4,
                  'HP': 15,
                  'Is Boss': False,
                  'Name': 'DB',
                  'Passive': None}
        self.assertEqual(expect, actual)

    @patch('random.randint', return_value=-3)
    def test_norm_monster_generator_Algorithm_with_neg_3(self, mock_random_num):
        actual = norm_monster_generator(self.character)
        expect = {'Damage': {'Max Damage': 4, 'Min Damage': 3},
                  'EXP': 4,
                  'HP': 20,
                  'Is Boss': False,
                  'Name': 'Algorithm',
                  'Passive': None}
        self.assertEqual(expect, actual)

    @patch('random.randint', return_value=-2)
    def test_norm_monster_generator_DataStructure_with_neg_2(self, mock_random_num):
        actual = norm_monster_generator(self.character)
        expect = {'Damage': {'Max Damage': 7, 'Min Damage': 2},
                  'EXP': 4,
                  'HP': 15,
                  'Is Boss': False,
                  'Name': 'DataStructure',
                  'Passive': None}
        self.assertEqual(expect, actual)

    @patch('random.randint', return_value=-1)
    def test_norm_monster_generator_DB_neg_1(self, mock_random_num):
        actual = norm_monster_generator(self.character)
        expect = {'Damage': {'Max Damage': 30, 'Min Damage': 1},
                  'EXP': 4,
                  'HP': 15,
                  'Is Boss': False,
                  'Name': 'DB',
                  'Passive': None}
        self.assertEqual(expect, actual)

    @patch('random.randint', return_value=0)
    def test_norm_monster_generator_OOP(self, mock_random_num):
        self.character["Level"] = 2
        actual = norm_monster_generator(self.character)
        expect = {'Damage': {'Max Damage': 7, 'Min Damage': 5},
                  'EXP': 4,
                  'HP': 30,
                  'Is Boss': False,
                  'Name': 'OOP',
                  'Passive': None}
        self.assertEqual(expect, actual)

    @patch('random.randint', return_value=1)
    def test_norm_monster_generator_SoftwareEngineering(self, mock_random_num):
        self.character["Level"] = 2
        actual = norm_monster_generator(self.character)
        expect = {'Damage': {'Max Damage': 10, 'Min Damage': 3},
                  'EXP': 4,
                  'HP': 20,
                  'Is Boss': False,
                  'Name': 'SoftwareEngineering',
                  'Passive': None}
        self.assertEqual(expect, actual)

    @patch('random.randint', return_value=2)
    def test_norm_monster_generator_AI_ML(self, mock_random_num):
        self.character["Level"] = 2
        actual = norm_monster_generator(self.character)
        expect = {'Damage': {'Max Damage': 60, 'Min Damage': 2},
                  'EXP': 4,
                  'HP': 15,
                  'Is Boss': False,
                  'Name': 'AI/ML',
                  'Passive': None}
        self.assertEqual(expect, actual)

    @patch('random.randint', return_value=0)
    def test_norm_monster_generator_invalid_level(self, mock_random_num):
        with self.assertRaises(KeyError):
            self.character["Level"] = 3
            norm_monster_generator(self.character)

    @patch('random.randint', return_value=-4)
    def test_norm_monster_generator_invalid_random_num_neg_4(self, mock_random_num):
        with self.assertRaises(IndexError):
            self.character["Level"] = 2
            norm_monster_generator(self.character)

    @patch('random.randint', return_value=3)
    def test_norm_monster_generator_invalid_random_num_3(self, mock_random_num):
        with self.assertRaises(IndexError):
            self.character["Level"] = 2
            norm_monster_generator(self.character)