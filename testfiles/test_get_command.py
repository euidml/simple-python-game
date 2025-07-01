from unittest import TestCase
from unittest.mock import patch
from game import get_command
import io


class Test(TestCase):

    @patch('builtins.input', side_effect=['1'])
    def test_get_command_attack_norm_monster(self, mock_input):
        actual = get_command(boss_mode=False)
        expect = "1"
        self.assertEqual(expect,actual)

    @patch('builtins.input', side_effect=['2'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_command_flee_norm_monster(self, mock_output, mock_input):
        actual_command = get_command(boss_mode=False)
        expect_command = "2"
        actual_msg = mock_output.getvalue()
        expect_msg = 'It\'s your turn! You can fight with the monster by typing "1" or you can flee from monster by ' \
                     '"2":\n'
        self.assertEqual(expect_msg, actual_msg)
        self.assertEqual(expect_command, actual_command)

    @patch('builtins.input', side_effect=['1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_command_attack_boss(self, mock_output, mock_input):
        actual_command = get_command(boss_mode=True)
        expect_command = "1"
        actual_msg = mock_output.getvalue()
        expect_msg = 'It\'s your turn! You can fight with the monster by typing "1":\n'
        self.assertEqual(expect_msg, actual_msg)
        self.assertEqual(expect_command, actual_command)

    # tests if user attempts to flee in boss mode.
    @patch('builtins.input', side_effect=['2', '1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_command_flee_boss(self, mock_output, mock_input):
        actual_command = get_command(boss_mode=True)
        expect_command = "1"
        actual_msg = mock_output.getvalue()
        expect_msg = "You cannot flee from the boss stage."
        self.assertIn(expect_msg, actual_msg)
        self.assertEqual(expect_command, actual_command)

    @patch('builtins.input', side_effect=['0', '', ' ', '!', 'attack', 'flee', '1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_command_invalid_inputs(self, mock_output, mock_input):
        actual_command = get_command(boss_mode=False)
        expect_command = "1"
        actual_msg = mock_output.getvalue()
        expect_msg = "Invalid command! Do it again"
        self.assertIn(expect_msg, actual_msg)
        self.assertEqual(expect_command, actual_command)