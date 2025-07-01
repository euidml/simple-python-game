from unittest import TestCase
from unittest.mock import patch
from game import show_result
import io


class Test(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_show_result_character_died(self, mock_stdout):
        show_result(is_char_alive=False, did_character_defeat_the_boss=False)
        expect = """
            ███████╗ ██████╗ ██████╗ ██████╗ ██╗   ██╗    ██╗   ██╗ ██████╗ ██╗   ██╗    ██████╗ ██╗███████╗██████╗ 
            ██╔════╝██╔═══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝    ╚██╗ ██╔╝██╔═══██╗██║   ██║    ██╔══██╗██║██╔════╝██╔══██╗
            ███████╗██║   ██║██████╔╝██████╔╝ ╚████╔╝      ╚████╔╝ ██║   ██║██║   ██║    ██║  ██║██║█████╗  ██║  ██║
            ╚════██║██║   ██║██╔══██╗██╔══██╗  ╚██╔╝        ╚██╔╝  ██║   ██║██║   ██║    ██║  ██║██║██╔══╝  ██║  ██║
            ███████║╚██████╔╝██║  ██║██║  ██║   ██║          ██║   ╚██████╔╝╚██████╔╝    ██████╔╝██║███████╗██████╔╝
            ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝          ╚═╝    ╚═════╝  ╚═════╝     ╚═════╝ ╚═╝╚══════╝╚═════╝                                                                                             
        
"""
        actual = mock_stdout.getvalue()
        self.assertEqual(expect, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_show_result_character_defeated_boss(self, mock_stdout):
        show_result(is_char_alive=True, did_character_defeat_the_boss=True)
        expect = """
             ██████╗ ██████╗ ███╗   ██╗ ██████╗ ██████╗  █████╗ ████████╗███████╗██╗
            ██╔════╝██╔═══██╗████╗  ██║██╔════╝ ██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██║
            ██║     ██║   ██║██╔██╗ ██║██║  ███╗██████╔╝███████║   ██║   ███████╗██║
            ██║     ██║   ██║██║╚██╗██║██║   ██║██╔══██╗██╔══██║   ██║   ╚════██║╚═╝
            ╚██████╗╚██████╔╝██║ ╚████║╚██████╔╝██║  ██║██║  ██║   ██║   ███████║██╗
             ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝
        
"""
        actual = mock_stdout.getvalue()
        self.assertEqual(expect, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_show_result_character_test_if_it_prints_nothing(self, mock_stdout):
        show_result(is_char_alive=True, did_character_defeat_the_boss=False)
        expect = ''
        actual = mock_stdout.getvalue()
        self.assertEqual(expect, actual)
