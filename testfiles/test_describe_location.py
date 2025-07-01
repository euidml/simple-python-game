from unittest import TestCase
from unittest.mock import patch
from game import describe_location
import io


class Test(TestCase):
    def setUp(self) -> None:
        self.rows = self.columns = 5
        self.board = {(0, 0): 'Room 645', (1, 0): 'Room 655', (2, 0): 'Room 655', (3, 0): 'Room 645', (4, 0): 'Room 682',
                 (0, 1): 'Room 645', (1, 1): 'Room 682', (2, 1): 'Room 655', (3, 1): 'Room 655', (4, 1): 'Room 682',
                 (0, 2): 'Room 682', (1, 2): 'Room 655', (2, 2): 'Room 655', (3, 2): 'Room 655', (4, 2): 'Room 655',
                 (0, 3): 'Room 655', (1, 3): 'Room 655', (2, 3): 'Room 682', (3, 3): 'Room 645', (4, 3): 'Room 645',
                 (0, 4): 'Room 645', (1, 4): 'Room 682', (2, 4): 'Room 682', (3, 4): 'Room 682', (4, 4): 'Room 645'}
        self.character = {"Location": {"X": 1, "Y": 1}, "Max HP": 100, "HP": 75, "Level": 1, "Level Name":\
    {"Level1": "CST student"}, "EXP": 1}

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_location_valid(self, mock_stdout):
        describe_location(self.board, self.columns, self.rows, self.character)
        actual = mock_stdout.getvalue()
        expect = """'🙂' is your current location. '😈' is boss room. '.' represent empty rooms.

 * ^ ^ * #
 * 🙂 ^ ^ #
 # ^ ^ ^ ^
 ^ ^ # * *
 * # # # 😈
HP: 75 Lv1: CST student EXP: 1

"""
        self.assertEqual(expect, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('game.character_icon_generator', return_value="\U0001F613")
    def test_describe_location_low_hp_emoji(self, mock_emoji, mock_stdout):
        describe_location(self.board, self.columns, self.rows, self.character)
        actual = mock_stdout.getvalue()
        expect = """'😓' is your current location. '😈' is boss room. '.' represent empty rooms.

 * ^ ^ * #
 * 😓 ^ ^ #
 # ^ ^ ^ ^
 ^ ^ # * *
 * # # # 😈
HP: 75 Lv1: CST student EXP: 1

"""
        self.assertEqual(expect, actual)

    # checking if the function modifies self.board correctly or not.
    def test_describe_location_check_if_it_modifies_board_data(self):
        self.character["Location"]["X"], self.character["Location"]["Y"] = 2, 2
        describe_location(self.board, self.columns, self.rows, self.character)
        emoji_char_actual = self.board[(self.character["Location"]["X"], self.character["Location"]["Y"])]
        emoji_char_expect = "Character"
        self.assertEqual(emoji_char_expect, emoji_char_actual)
