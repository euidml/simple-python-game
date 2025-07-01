from unittest import TestCase
from unittest.mock import patch
from game import get_user_choice
import io


class Test(TestCase):

    @patch('builtins.input', side_effect=['1'])
    def test_get_user_choice_north(self, mock_output):
        actual = get_user_choice()
        expect = (0, -1)
        self.assertEqual(expect, actual)

    @patch('builtins.input', side_effect=['2'])
    def test_get_user_choice_south(self, mock_input):
        actual = get_user_choice()
        expect = (0, 1)
        self.assertEqual(expect, actual)

    @patch('builtins.input', side_effect=['3'])
    def test_get_user_choice_west(self, mock_input):
        actual = get_user_choice()
        expect = (-1, 0)
        self.assertEqual(expect, actual)

    @patch('builtins.input', side_effect=['4'])
    def test_get_user_choice_east(self, mock_input):
        actual = get_user_choice()
        expect = (1, 0)
        self.assertEqual(expect, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['', '0', '-1', ' ', 'north', '1'])
    def test_get_user_choice_invalid_inputs(self, mock_input, mock_output):
        get_user_choice()
        actual = mock_output.getvalue()
        expect = "Decide where to go... \n1) goes to the north\n2) goes to the south\n3) goes to the west\n4) goes to "\
                 "the east\nInvalid Input(s)\n\nInvalid Input(s)\n\nInvalid Input(s)\n\nInvalid Input(s)\n\nInvalid " \
                 "Input(s)\n\n"
        self.assertEqual(expect, actual)

