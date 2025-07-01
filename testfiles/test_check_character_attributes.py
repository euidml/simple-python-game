from unittest import TestCase
from unittest.mock import patch
from game import check_character_attributes
import io


class Test(TestCase):

    def setUp(self) -> None:
        self.character_python_warrior = {'Adding Level Up Attr Amount': {'Max Damage': 10, 'Max HP': 30,
                                                                         'Min Damage': 10},
                                         'Class': 'python warrior', 'Damage': {'Max Damage': 12, 'Min Damage': 9},
                                         'EXP': 0,
                                         'HP': 100, 'Level': 1,
                                         'Level Name': {'Level1': 'python soldier', 'Level2': 'python warrior',
                                                        'Level3': 'python hero'},
                                         'Location': {'X': 2, 'Y': 2}, 'Max HP': 100, 'Name': 'Edward',
                                         'Passive': 'pythonic'}

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('game.check_level_up', return_value=False)
    def test_check_character_python_warrior_attributes_valid_declining_level_up(self, mock_level_up, mock_stdout):
        check_character_attributes(self.character_python_warrior)
        actual = mock_stdout.getvalue()
        expect = ""
        self.assertEqual(expect, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_character_python_warrior_attributes_valid_processing_level_up_2(self, mock_stdout):
        self.character_python_warrior["EXP"] = 10
        check_character_attributes(self.character_python_warrior)
        actual_msg = mock_stdout.getvalue()
        expect_msg = "Congrats! You leveled up. And now you are python warrior\n"
        actual_attr = self.character_python_warrior
        expect_attr = {'Adding Level Up Attr Amount': {'Max Damage': 10,
                                                       'Max HP': 30,
                                                       'Min Damage': 10},
                       'Class': 'python warrior',
                       'Damage': {'Max Damage': 22, 'Min Damage': 19},
                       'EXP': 0,
                       'HP': 130,
                       'Level': 2,
                       'Level Name': {'Level1': 'python soldier',
                                      'Level2': 'python warrior',
                                      'Level3': 'python hero'},
                       'Location': {'X': 2, 'Y': 2},
                       'Max HP': 130,
                       'Name': 'Edward',
                       'Passive': 'pythonic'}
        self.assertEqual(expect_msg, actual_msg)
        self.assertEqual(expect_attr, actual_attr)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_character_python_warrior_attributes_valid_processing_level_up_3(self, mock_stdout):
        self.character_python_warrior, self.character_python_warrior["EXP"] = {'Adding Level Up Attr Amount': {
            'Max Damage': 10,
            'Max HP': 30,
            'Min Damage': 10},
                                                                                  'Class': 'python warrior',
                                                                                  'Damage': {'Max Damage': 22,
                                                                                             'Min Damage': 19},
                                                                                  'EXP': 0,
                                                                                  'HP': 130,
                                                                                  'Level': 2,
                                                                                  'Level Name': {
                                                                                      'Level1': 'python soldier',
                                                                                      'Level2': 'python warrior',
                                                                                      'Level3': 'python hero'},
                                                                                  'Location': {'X': 2, 'Y': 2},
                                                                                  'Max HP': 130,
                                                                                  'Name': 'Edward',
                                                                                  'Passive': 'pythonic'}, 10
        check_character_attributes(self.character_python_warrior)
        actual_msg = mock_stdout.getvalue()
        expect_msg = "Congrats! You leveled up. And now you are python hero\n"
        actual_attr = self.character_python_warrior
        expect_attr = {'Adding Level Up Attr Amount': {'Max Damage': 10,
                                                       'Max HP': 30,
                                                       'Min Damage': 10},
                       'Class': 'python warrior',
                       'Damage': {'Max Damage': 32, 'Min Damage': 29},
                       'EXP': 0,
                       'HP': 160,
                       'Level': 3,
                       'Level Name': {'Level1': 'python soldier',
                                      'Level2': 'python warrior',
                                      'Level3': 'python hero'},
                       'Location': {'X': 2, 'Y': 2},
                       'Max HP': 160,
                       'Name': 'Edward',
                       'Passive': 'pythonic'}
        self.assertEqual(expect_msg, actual_msg)
        self.assertEqual(expect_attr, actual_attr)

    # try to level up even though character's EXP is not sufficient to get leveled up
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('game.check_level_up', return_value=True)
    def test_check_character_attributes_invalid_processing_level_up_2(self, mock_level_up, mock_stdout):
        check_character_attributes(self.character_python_warrior)
        actual_msg = mock_stdout.getvalue()
        expect_msg = "Congrats! You leveled up. And now you are python warrior\n"
        actual_attr = self.character_python_warrior
        expect_attr = {'Adding Level Up Attr Amount': {'Max Damage': 10,
                                                       'Max HP': 30,
                                                       'Min Damage': 10},
                       'Class': 'python warrior',
                       'Damage': {'Max Damage': 22, 'Min Damage': 19},
                       'EXP': 0,
                       'HP': 130,
                       'Level': 2,
                       'Level Name': {'Level1': 'python soldier',
                                      'Level2': 'python warrior',
                                      'Level3': 'python hero'},
                       'Location': {'X': 2, 'Y': 2},
                       'Max HP': 130,
                       'Name': 'Edward',
                       'Passive': 'pythonic'}
        self.assertEqual(expect_msg, actual_msg)
        self.assertEqual(expect_attr, actual_attr)

