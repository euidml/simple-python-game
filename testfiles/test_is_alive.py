from unittest import TestCase
from game import is_alive


class Test(TestCase):

    def test_is_alive_positive_num(self):
        actual = is_alive(75)
        self.assertTrue(actual)

    def test_is_alive_negative_num(self):
        actual = is_alive(-10)
        self.assertFalse(actual)

    def test_is_alive_zero(self):
        actual = is_alive(0)
        self.assertFalse(actual)
