from unittest import TestCase
from unittest.mock import patch
from game import fight
import io


class Test(TestCase):

    def setUp(self) -> None:
        self.character = {'Class': 'python warrior', 'Damage': {'Max Damage': 12, 'Min Damage': 10},
                          'EXP': 0,
                          'HP': 20, 'Level': 1,
                          'Level Name': {'Level1': 'python soldier', 'Level2': 'python warrior',
                                         'Level3': 'python hero'}, 'Name': 'Edward',
                          'Passive': 'pythonic'}
        self.monster = {"Name": "Algorithm", "Passive": None, "Is Boss": False, "HP": 20, "EXP": 4,
                        "Damage": {"Max Damage": 4, "Min Damage": 3}}

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('game.get_command', return_value='2')
    def test_fight_character_flee(self, mock_command, mock_output):
        fight(self.character, self.monster)
        actual = mock_output.getvalue()
        expect = "Edward: 20, Algorithm: 20\nWhoo! Let's run away from Algorithm!\n"
        self.assertEqual(expect, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('game.is_flee', return_value=True)
    @patch('game.get_command', return_value='0')
    def test_fight_monster_flee(self, mock_command, mock_flee, mock_output):
        actual_flee = fight(self.character, self.monster)
        actual_msg = mock_output.getvalue()
        expect_msg = "Algorithm has fled away!\n"
        self.assertIn(expect_msg, actual_msg)
        self.assertFalse(actual_flee)

    @patch('game.get_command', return_value='1')
    @patch('game.is_flee', return_value=False)
    @patch('game.get_command', return_value='1')
    def test_fight_defeating_monster(self, mock_command_1, mock_flee, mock_command_2):
        actual = fight(self.character, self.monster)
        self.assertTrue(actual)

    @patch('game.is_flee', return_value=False)
    @patch('game.get_command', return_value='1')
    def test_fight_character_die(self, mock_command_1, mock_flee):
        self.character["HP"] = 1
        actual = fight(self.character, self.monster)
        self.assertFalse(actual)
