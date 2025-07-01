from unittest import TestCase
from game import boss_monster_generator


class Test(TestCase):
    def setUp(self) -> None:
        self.character = {"Passive": "pythonic"}

    def test_boss_monster_generator_valid(self):
        actual = boss_monster_generator(self.character)
        expect = {'Damage': {'Max Damage': 20, 'Min Damage': 10},
                  'EXP': 0,
                  'HP': 100,
                  'Is Boss': True,
                  'Name': 'The Exam Dragon',
                  'Passive': 'pythonic'}
        self.assertEqual(expect, actual)

    def test_boss_monster_generator_invalid_damage(self):
        actual = boss_monster_generator(self.character)
        expect = {'Max Damage': 60, 'Min Damage': -10}
        self.assertNotEqual(expect, actual["Damage"])

    def test_boss_monster_generator_invalid_exp(self):
        actual = boss_monster_generator(self.character)
        expect = -1
        self.assertNotEqual(expect, actual["EXP"])

    def test_boss_monster_generator_invalid_HP(self):
        actual = boss_monster_generator(self.character)
        expect = 99
        self.assertNotEqual(expect, actual["HP"])

    def test_boss_monster_generator_invalid_boss_mode(self):
        actual = boss_monster_generator(self.character)
        expect = False
        self.assertNotEqual(expect, actual["Is Boss"])

    def test_boss_monster_generator_invalid_name(self):
        actual = boss_monster_generator(self.character)
        expect = "The Exam Snake"
        self.assertNotEqual(expect, actual["Name"])

    def test_boss_monster_generator_invalid_passive(self):
        actual = boss_monster_generator(self.character)
        expect = "agile"
        self.assertNotEqual(expect, actual["Passive"])

