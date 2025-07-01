from unittest import TestCase
from unittest.mock import patch
from game import get_name
import io


class Test(TestCase):

    @patch('builtins.input', side_effect=['edward'])
    def test_get_name_input_edward(self, mock_input):
        expect = "Edward"
        actual = get_name()
        self.assertEqual(expect, actual)

    @patch('builtins.input', side_effect=['chris'])
    def test_get_name_input_chris(self, mock_input):
        expect = "Chris"
        actual = get_name()
        self.assertEqual(expect, actual)

    # throws invalid cases first and throw a valid case at last in order to stop the iteration
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['', '!', '\n', ' ', '1', 'edward'])
    def test_get_name_input_invalid_name(self, mock_input, mock_stdout):
        get_name()
        expect = 'Invalid name! Do it again\nInvalid name! Do it again\nInvalid name! Do it again\nInvalid name! ' \
                 'Do it again\nInvalid name! Do it again\n'
        actual = mock_stdout.getvalue()
        self.assertEqual(expect, actual)
