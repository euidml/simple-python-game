from unittest import TestCase
from unittest.mock import patch
from game import make_board


# this test is to see if the function stores x * y map. It is not to see if the room names are generated correctly
class Test(TestCase):

    @patch('game.room_generator', return_value='Room 645')
    def test_make_board_pos_rows_columns(self, mock_room_names):
        actual = make_board(rows=5, columns=5)
        expect = {(0, 0): 'Room 645',
                  (0, 1): 'Room 645',
                  (0, 2): 'Room 645',
                  (0, 3): 'Room 645',
                  (0, 4): 'Room 645',
                  (1, 0): 'Room 645',
                  (1, 1): 'Room 645',
                  (1, 2): 'Room 645',
                  (1, 3): 'Room 645',
                  (1, 4): 'Room 645',
                  (2, 0): 'Room 645',
                  (2, 1): 'Room 645',
                  (2, 2): 'Room 645',
                  (2, 3): 'Room 645',
                  (2, 4): 'Room 645',
                  (3, 0): 'Room 645',
                  (3, 1): 'Room 645',
                  (3, 2): 'Room 645',
                  (3, 3): 'Room 645',
                  (3, 4): 'Room 645',
                  (4, 0): 'Room 645',
                  (4, 1): 'Room 645',
                  (4, 2): 'Room 645',
                  (4, 3): 'Room 645',
                  (4, 4): 'Room 645'}
        self.assertEqual(expect, actual)

    @patch('game.room_generator', return_value='Room 655')
    def test_make_board_neg_rows_columns(self, mock_room_names):
        actual = make_board(rows=-3, columns=-3)
        expect = {}
        self.assertEqual(expect, actual)

    @patch('game.room_generator', return_value='Room 682')
    def test_make_board_neg_rows_pos_columns(self, mock_room_names):
        actual = make_board(rows=-3, columns=3)
        expect = {}
        self.assertEqual(expect, actual)

    @patch('game.room_generator', return_value='Room 682')
    def test_make_board_zero_rows_columns(self, mock_room_names):
        actual = make_board(rows=0, columns=0)
        expect = {}
        self.assertEqual(expect, actual)
