from unittest import TestCase
from game import move_character


class Test(TestCase):
    def setUp(self) -> None:
        self.board = {(0, 0): 'A', (1, 0): 'B', (2, 0): 'A', (0, 1): 'C',
                      (1, 1): 'C', (2, 1): 'A', (0, 2): 'B', (1, 2): 'A',
                      (2, 2): 'C'}
        self.character = {"Location": {"X": 0, "Y": 0}}

    def test_move_character_test_valid_case_south(self):
        actual_key = (self.character["Location"]["X"], self.character["Location"]["Y"])
        direction = (0, 1)
        move_character(self.board, self.character, direction)
        actual_room_name = self.board[actual_key]
        expect_room_name = "Empty Room"
        actual_char_location = self.character["Location"]["Y"]
        expect_char_location = 1
        self.assertEqual(actual_room_name, expect_room_name)
        self.assertEqual(expect_char_location, actual_char_location)

    def test_move_character_test_valid_case_east(self):
        actual_key = (self.character["Location"]["X"], self.character["Location"]["Y"])
        direction = (1, 0)
        move_character(self.board, self.character, direction)
        actual_room_name = self.board[actual_key]
        expect_room_name = "Empty Room"
        actual_char_location = self.character["Location"]["X"]
        expect_char_location = 1
        self.assertEqual(actual_room_name, expect_room_name)
        self.assertEqual(expect_char_location, actual_char_location)

    def test_move_character_test_valid_case_north(self):
        self.character["Location"]["X"], self.character["Location"]["Y"] = 2, 2
        actual_key = (self.character["Location"]["X"], self.character["Location"]["Y"])
        direction = (0, -1)
        move_character(self.board, self.character, direction)
        actual_room_name = self.board[actual_key]
        expect_room_name = "Empty Room"
        actual_char_location = self.character["Location"]["Y"]
        expect_char_location = 1
        self.assertEqual(actual_room_name, expect_room_name)
        self.assertEqual(expect_char_location, actual_char_location)

    def test_move_character_test_valid_case_west(self):
        self.character["Location"]["X"], self.character["Location"]["Y"] = 2, 2
        actual_key = (self.character["Location"]["X"], self.character["Location"]["Y"])
        direction = (-1, 0)
        move_character(self.board, self.character, direction)
        actual_room_name = self.board[actual_key]
        expect_room_name = "Empty Room"
        actual_char_location = self.character["Location"]["X"]
        expect_char_location = 1
        self.assertEqual(actual_room_name, expect_room_name)
        self.assertEqual(expect_char_location, actual_char_location)

    def test_move_character_test_invalid_case_east(self):
        direction = (-1, 0)
        move_character(self.board, self.character, direction)
        actual = (self.character["Location"]["X"], self.character["Location"]["Y"]) in self.board
        self.assertFalse(actual)

    def test_move_character_test_invalid_case_north(self):
        direction = (0, -1)
        move_character(self.board, self.character, direction)
        actual = (self.character["Location"]["X"], self.character["Location"]["Y"]) in self.board
        self.assertFalse(actual)

    def test_move_character_test_invalid_case_west(self):
        self.character["Location"]["X"], self.character["Location"]["Y"] = 2, 2
        direction = (1, 0)
        move_character(self.board, self.character, direction)
        actual = (self.character["Location"]["X"], self.character["Location"]["Y"]) in self.board
        self.assertFalse(actual)

    def test_move_character_test_invalid_case_south(self):
        self.character["Location"]["X"], self.character["Location"]["Y"] = 2, 2
        direction = (0, 1)
        move_character(self.board, self.character, direction)
        actual = (self.character["Location"]["X"], self.character["Location"]["Y"]) in self.board
        self.assertFalse(actual)
