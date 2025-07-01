from unittest import TestCase
from unittest.mock import patch
from game import damage_dodger


class Test(TestCase):

    def setUp(self) -> None:
        self.non_security_character = {'Class': 'python warrior', 'Damage': {'Max Damage': 12, 'Min Damage': 10},
                                       'EXP': 0, 'HP': 20, 'Level': 1, 'Name': 'Edward', 'Passive': 'pythonic'}
        self.security_character = {'Class': 'db guardian', 'Damage': {'Max Damage': 12, 'Min Damage': 10},
                                   'EXP': 0, 'HP': 20, 'Level': 1, 'Name': 'Edward', 'Passive': 'security'}

    @patch('random.randint', return_value=1)
    def test_damage_dodger_non_security_character_not_in_chance_1(self, mock_random_num):
        actual = damage_dodger(self.non_security_character)
        self.assertFalse(actual)

    @patch('random.randint', return_value=2)
    def test_damage_dodger_non_security_character_not_in_chance_2(self, mock_random_num):
        actual = damage_dodger(self.non_security_character)
        self.assertFalse(actual)

    @patch('random.randint', return_value=0)
    def test_damage_dodger_non_security_character_in_chance(self, mock_random_num):
        actual = damage_dodger(self.non_security_character)
        self.assertFalse(actual)

    @patch('random.randint', return_value=1)
    def test_damage_dodger_security_character_not_in_chance_1(self, mock_random_num):
        actual = damage_dodger(self.security_character)
        self.assertFalse(actual)

    @patch('random.randint', return_value=2)
    def test_damage_dodger_security_character_not_in_chance_2(self, mock_random_num):
        actual = damage_dodger(self.security_character)
        self.assertFalse(actual)

    @patch('random.randint', return_value=-1)
    def test_damage_dodger_security_character_not_in_chance_neg_1(self, mock_random_num):
        actual = damage_dodger(self.security_character)
        self.assertFalse(actual)

    @patch('random.randint', return_value=0)
    def test_damage_dodger_security_character_in_chance(self, mock_random_num):
        actual = damage_dodger(self.security_character)
        self.assertTrue(actual)
