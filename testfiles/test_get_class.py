from unittest import TestCase
from unittest.mock import patch
from game import get_class
import io


class Test(TestCase):

    def setUp(self) -> None:
        self.class_list = ("python warrior", "web dev assassin", "db guardian", "project sorcerer")

    @patch('builtins.input', side_effect=['1'])
    def test_get_class_input_1_python_warrior(self, mock_input):
        actual = get_class(class_list=self.class_list)
        expect = 'python warrior'
        self.assertEqual(expect, actual)

    @patch('builtins.input', side_effect=['2'])
    def test_get_class_input_2_web_dev_assassin(self, mock_input):
        actual = get_class(class_list=self.class_list)
        expect = "web dev assassin"
        self.assertEqual(expect, actual)

    @patch('builtins.input', side_effect=['3'])
    def test_get_class_input_3_db_guardian(self, mock_input):
        actual = get_class(class_list=self.class_list)
        expect = "db guardian"
        self.assertEqual(expect, actual)

    @patch('builtins.input', side_effect=['4'])
    def test_get_class_input_4_project_sorcerer(self, mock_input):
        actual = get_class(class_list=self.class_list)
        expect = "project sorcerer"
        self.assertEqual(expect, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['!', 'e', '', ' ', '5', '1'])
    def test_get_class_input_invalid_case_raise_ValueError_and_IndexError(self, mock_input, mock_stdout):
        get_class(class_list=self.class_list)
        actual = mock_stdout.getvalue()
        expect = "\nChoose your Class:\n1) python warrior\n2) web dev assassin\n3) db guardian\n4) project sorcerer" \
                 "\n\nType correct class name.\n\nType correct class name.\n\nType correct class name.\n\nType " \
                 "correct class name.\n\nType correct class name.\n\n"
        self.assertEqual(expect, actual)
