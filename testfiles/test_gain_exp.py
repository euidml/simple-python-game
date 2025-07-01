from unittest import TestCase
from unittest.mock import patch
from game import gain_exp
import io


class Test(TestCase):

    def setUp(self) -> None:
        self.agile_character = {"Name": "Edward", "EXP": 1, "Passive": "agile"}
        self.non_agile_character = {"Name": "Chris", "EXP": 1, "Passive": "pythonic"}
        self.monster = {"Name": "Algorithm", "EXP": 3}

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_gain_exp_non_agile(self, mock_stdout):
        gain_exp(self.non_agile_character, self.monster)
        actual_stdout = mock_stdout.getvalue()
        expect_stdout = 'Chris got 3 exp defeating Algorithm\n'
        actual_exp_amt = self.non_agile_character["EXP"]
        expect_exp_amt = 4
        self.assertEqual(expect_stdout, actual_stdout)
        self.assertEqual(expect_exp_amt, actual_exp_amt)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_gain_exp_agile(self, mock_stdout):
        gain_exp(self.agile_character, self.monster)
        actual_stdout = mock_stdout.getvalue()
        expect_stdout = 'Edward got 6 exp defeating Algorithm\n'
        actual_exp_amt = self.agile_character["EXP"]
        expect_exp_amt = 7
        self.assertEqual(expect_stdout, actual_stdout)
        self.assertEqual(expect_exp_amt, actual_exp_amt)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_gain_exp_0(self, mock_stdout):
        self.monster["EXP"] = 0
        gain_exp(self.non_agile_character, self.monster)
        actual_stdout = mock_stdout.getvalue()
        expect_stdout = 'Chris got 0 exp defeating Algorithm\n'
        actual_exp_amt = self.non_agile_character["EXP"]
        expect_exp_amt = 1
        self.assertEqual(expect_stdout, actual_stdout)
        self.assertEqual(expect_exp_amt, actual_exp_amt)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_gain_exp_neg_num(self, mock_stdout):
        self.monster["EXP"] = -2
        gain_exp(self.non_agile_character, self.monster)
        actual_stdout = mock_stdout.getvalue()
        expect_stdout = 'Chris got -2 exp defeating Algorithm\n'
        actual_exp_amt = self.non_agile_character["EXP"]
        expect_exp_amt = -1
        self.assertEqual(expect_stdout, actual_stdout)
        self.assertEqual(expect_exp_amt, actual_exp_amt)

    # although it exceeds the amount of exp to get leveled up which is 10, but it stays because here is not processing
    # to get leveled up.
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_gain_exp_over_10(self, mock_stdout):
        self.monster["EXP"] = 5
        gain_exp(self.agile_character, self.monster)
        actual_stdout = mock_stdout.getvalue()
        expect_stdout = 'Edward got 10 exp defeating Algorithm\n'
        actual_exp_amt = self.agile_character["EXP"]
        expect_exp_amt = 11
        self.assertEqual(expect_stdout, actual_stdout)
        self.assertEqual(expect_exp_amt, actual_exp_amt)