from unittest import TestCase
from unittest.mock import patch
from game import room_generator


class Test(TestCase):

    @patch('random.randint', side_effect=[0])
    def test_room_generator_room_645(self, mock_random_num):
        actual = room_generator()
        expect = 'Room 645'
        self.assertEqual(expect, actual)

    @patch('random.randint', side_effect=[1])
    def test_room_generator_room_655(self, mock_random_num):
        actual = room_generator()
        expect = 'Room 655'
        self.assertEqual(expect, actual)

    @patch('random.randint', side_effect=[2])
    def test_room_generator_room_682(self, mock_random_num):
        actual = room_generator()
        expect = 'Room 682'
        self.assertEqual(expect, actual)

    # it recognizes [-1, -3] for indices because it is a tuple
    @patch('random.randint', side_effect=[-1])
    def test_room_generator_room_682_with_negative_1(self, mock_random_num):
        actual = room_generator()
        expect = 'Room 682'
        self.assertEqual(expect, actual)

    @patch('random.randint', side_effect=[-2])
    def test_room_generator_room_655_with_negative_2(self, mock_random_num):
        actual = room_generator()
        expect = 'Room 655'
        self.assertEqual(expect, actual)

    @patch('random.randint', side_effect=[-3])
    def test_room_generator_room_645_with_negative_3(self, mock_random_num):
        actual = room_generator()
        expect = 'Room 645'
        self.assertEqual(expect, actual)

    @patch('random.randint', side_effect=[4])
    def test_room_generator_raise_Indexerror_1(self, mock_random_num):
        with self.assertRaises(IndexError):
            room_generator()

    @patch('random.randint', side_effect=[-4])
    def test_room_generator_raise_Indexerror_2(self, mock_random_num):
        with self.assertRaises(IndexError):
            room_generator()

