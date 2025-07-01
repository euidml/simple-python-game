from unittest import TestCase
from unittest.mock import patch
from game import is_flee


class Test(TestCase):

    @patch('random.randint', return_value=1)
    def test_is_flee_not_boss_mode_valid_False_1(self, mock_random_num):
        actual = is_flee(False)
        self.assertFalse(actual)

    @patch('random.randint', return_value=2)
    def test_is_flee_not_boss_mode_valid_False_2(self, mock_random_num):
        actual = is_flee(False)
        self.assertFalse(actual)

    @patch('random.randint', return_value=3)
    def test_is_flee_not_boss_mode_valid_False_3(self, mock_random_num):
        actual = is_flee(False)
        self.assertFalse(actual)

    @patch('random.randint', return_value=4)
    def test_is_flee_not_boss_mode_valid_False_4(self, mock_random_num):
        actual = is_flee(False)
        self.assertFalse(actual)

    @patch('random.randint', return_value=0)
    def test_is_flee_not_boss_mode_valid_True(self, mock_random_num):
        actual = is_flee(False)
        self.assertTrue(actual)

    @patch('random.randint', return_value=-1)
    def test_is_flee_not_boss_mode_invalid_False_neg_1(self, mock_random_num):
        actual = is_flee(False)
        self.assertFalse(actual)

    @patch('random.randint', return_value=5)
    def test_is_flee_not_boss_mode_invalid_False_5(self, mock_random_num):
        actual = is_flee(False)
        self.assertFalse(actual)

    @patch('random.randint', return_value=0)
    def test_is_flee_boss_mode_valid_False_0(self, mock_random_num):
        actual = is_flee(True)
        self.assertFalse(actual)

    @patch('random.randint', return_value=4)
    def test_is_flee_boss_mode_valid_False_4(self, mock_random_num):
        actual = is_flee(True)
        self.assertFalse(actual)

    @patch('random.randint', return_value=-1)
    def test_is_flee_boss_mode_invalid_False_neg_1(self, mock_random_num):
        actual = is_flee(True)
        self.assertFalse(actual)

    @patch('random.randint', return_value=-1)
    def test_is_flee_boss_mode_invalid_False_5(self, mock_random_num):
        actual = is_flee(True)
        self.assertFalse(actual)
