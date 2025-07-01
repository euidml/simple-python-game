from unittest import TestCase
from unittest.mock import patch
from game import fight_with_boss
import io


class Test(TestCase):
    def setUp(self) -> None:
        self.character = {"Level": 1, "Level Name": {
            "Level1": "python soldier", "Level2": "python warrior", "Level3": "python hero",
        }, "Passive": "pythonic"}

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('game.fight', return_value=False)
    def test_fight_with_boss_level_1_character_lost(self, mock_fight, mock_stdout):
        actual_result = fight_with_boss(self.character)
        actual_msg = mock_stdout.getvalue()
        expect_msg = "Finally You, python soldier faced The Exam Dragon. You need to have an endless fight with that" \
                     " dragon!"
        self.assertFalse(actual_result)
        self.assertIn(expect_msg, actual_msg)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('game.fight', return_value=False)
    def test_fight_with_boss_level_2_character_lost(self, mock_fight, mock_stdout):
        self.character["Level"] = 2
        actual_result = fight_with_boss(self.character)
        actual_msg = mock_stdout.getvalue()
        expect_msg = "Finally You, python warrior faced The Exam Dragon. You need to have an endless fight with that" \
                     " dragon!"
        self.assertFalse(actual_result)
        self.assertIn(expect_msg, actual_msg)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('game.fight', return_value=True)
    def test_fight_with_boss_level_3_character_defeated_boss(self, mock_fight, mock_stdout):
        self.character["Level"] = 3
        actual_result = fight_with_boss(self.character)
        actual_msg = mock_stdout.getvalue()
        expect_msg = "Finally You, python hero faced The Exam Dragon. You need to have an endless fight with that" \
                     " dragon!"
        self.assertTrue(actual_result)
        self.assertIn(expect_msg, actual_msg)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('game.fight', return_value=True)
    def test_fight_with_boss_level_4_character_defeated_boss(self, mock_fight, mock_stdout):
        with self.assertRaises(KeyError):
            self.character["Level"] = 4
            fight_with_boss(self.character)
