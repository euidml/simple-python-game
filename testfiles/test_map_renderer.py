from unittest import TestCase
from unittest.mock import patch
from game import map_renderer
import io


class Test(TestCase):

    def setUp(self) -> None:
        self.rows = self.columns = 5
        self.board = {(0, 0): 'Room 645', (1, 0): 'Room 655', (2, 0): 'Room 655', (3, 0): 'Room 645',
                      (4, 0): 'Character',
                      (0, 1): 'Room 645', (1, 1): 'Room 682', (2, 1): 'Room 655', (3, 1): 'Room 655',
                      (4, 1): 'Room 682',
                      (0, 2): 'Room 682', (1, 2): 'Room 655', (2, 2): 'Room 655', (3, 2): 'Room 655',
                      (4, 2): 'Room 655',
                      (0, 3): 'Room 655', (1, 3): 'Room 655', (2, 3): 'Room 682', (3, 3): 'Room 645',
                      (4, 3): 'Room 645',
                      (0, 4): 'Room 645', (1, 4): 'Room 682', (2, 4): 'Room 682', (3, 4): 'Room 682',
                      (4, 4): 'Destination'}
        self.character_icon = "\U0001F601"

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_map_renderer_test_printing_5x5 (self, mock_stdout):
        map_renderer(self.board, self.columns, self.rows, self.character_icon)
        actual = mock_stdout.getvalue()
        expect = " * ^ ^ * 😁\n * # ^ ^ #\n # ^ ^ ^ ^\n ^ ^ # * *\n * # # # 😈\n"
        self.assertEqual(expect, actual)

    # testing how the function prints the map 5 * 5 map as 3 * 3 sized
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_map_renderer_test_printing_smaller_map(self, mock_stdout):
        self.rows = self.columns = 3
        map_renderer(self.board, self.columns, self.rows, self.character_icon)
        actual = mock_stdout.getvalue()
        expect = " * ^ ^\n * # ^\n # ^ ^\n"
        self.assertEqual(expect, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_map_renderer_test_printing_1x1_map(self, mock_stdout):
        self.rows = self.columns = 1
        map_renderer(self.board, self.columns, self.rows, self.character_icon)
        actual = mock_stdout.getvalue()
        expect = " *\n"
        self.assertEqual(expect, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_map_renderer_test_printing_0_rows_columns(self, mock_stdout):
        self.rows = self.columns = -2
        map_renderer(self.board, self.columns, self.rows, self.character_icon)
        actual = mock_stdout.getvalue()
        expect = ""
        self.assertEqual(expect, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_map_renderer_test_printing_negative_rows_columns(self, mock_stdout):
        self.rows = self.columns = -2
        map_renderer(self.board, self.columns, self.rows, self.character_icon)
        actual = mock_stdout.getvalue()
        expect = ""
        self.assertEqual(expect, actual)
