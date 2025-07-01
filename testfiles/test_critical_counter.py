from unittest import TestCase
from unittest.mock import patch
from game import critical_counter
import io


class Test(TestCase):

    def setUp(self) -> None:
        self.non_employ_legend_character = {'Class': 'python warrior', 'Damage': {'Max Damage': 12, 'Min Damage': 10},
                                            'EXP': 0,
                                            'HP': 20, 'Level': 1,
                                            'Level Name': {'Level1': 'python soldier', 'Level2': 'python warrior',
                                                           'Level3': 'python hero'}, 'Name': 'Edward',
                                            'Passive': 'pythonic'}
        self.employ_legend_character = {'Class': 'python warrior', 'Damage': {'Max Damage': 12, 'Min Damage': 10},
                                        'EXP': 0,
                                        'HP': 20, 'Level': 1,
                                        'Level Name': {'Level1': 'python soldier', 'Level2': 'python warrior',
                                                       'Level3': 'python hero'}, 'Name': 'Edward',
                                        'Passive': "employ's legend"}

    @patch('random.randint', return_value=0)
    def test_critical_counter_non_employ_legend_normal_dmg_0(self, mock_random):
        actual_dmg = critical_counter(self.non_employ_legend_character)
        expect_dmg = 10
        self.assertEqual(expect_dmg, actual_dmg)

    @patch('random.randint', return_value=1)
    def test_critical_counter_non_employ_legend_normal_dmg_1(self, mock_random):
        actual_dmg = critical_counter(self.non_employ_legend_character)
        expect_dmg = 10
        self.assertEqual(expect_dmg, actual_dmg)

    @patch('random.randint', return_value=2)
    def test_critical_counter_non_employ_legend_normal_dmg_2(self, mock_random):
        actual_dmg = critical_counter(self.non_employ_legend_character)
        expect_dmg = 10
        self.assertEqual(expect_dmg, actual_dmg)

    @patch('random.randint', return_value=3)
    def test_critical_counter_non_employ_legend_critical_dmg(self, mock_random):
        actual_dmg = critical_counter(self.non_employ_legend_character)
        expect_dmg = 12
        self.assertEqual(expect_dmg, actual_dmg)

    @patch('random.randint', return_value=-1)
    def test_critical_counter_non_employ_legend_normal_dmg_invalid_rand_num_1(self, mock_random):
        actual_dmg = critical_counter(self.non_employ_legend_character)
        expect_dmg = 10
        self.assertEqual(expect_dmg, actual_dmg)

    @patch('random.randint', return_value=4)
    def test_critical_counter_non_employ_legend_normal_dmg_invalid_rand_num_2(self, mock_random):
        actual_dmg = critical_counter(self.non_employ_legend_character)
        expect_dmg = 10
        self.assertEqual(expect_dmg, actual_dmg)

    # there are only 0, 1 for valid random numbers.
    @patch('random.randint', return_value=0)
    def test_critical_counter_employ_legend_normal_dmg_0(self, mock_random):
        actual_dmg = critical_counter(self.employ_legend_character)
        expect_dmg = 10
        self.assertEqual(expect_dmg, actual_dmg)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', return_value=1)
    def test_critical_counter_employ_legend_critical_dmg(self, mock_random, mock_stdout):
        actual_dmg = critical_counter(self.employ_legend_character)
        expect_dmg = 12
        actual_msg = mock_stdout.getvalue()
        expect_msg = 'Edward used "employ\'s legend"!\n'
        self.assertEqual(expect_dmg, actual_dmg)
        self.assertEqual(expect_msg, actual_msg)

    @patch('random.randint', return_value=-1)
    def test_critical_counter_employ_legend_normal_dmg_invalid_rand_num_1(self, mock_random):
        actual_dmg = critical_counter(self.employ_legend_character)
        expect_dmg = 10
        self.assertEqual(expect_dmg, actual_dmg)

    @patch('random.randint', return_value=2)
    def test_critical_counter_employ_legend_normal_dmg_invalid_rand_num_2(self, mock_random):
        actual_dmg = critical_counter(self.employ_legend_character)
        expect_dmg = 10
        self.assertEqual(expect_dmg, actual_dmg)
