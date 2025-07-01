from unittest import TestCase
from unittest.mock import patch
from game import attack
import io


class Test(TestCase):

    def setUp(self) -> None:
        self.non_security_character = {'Class': 'python warrior', 'Damage': {'Max Damage': 12, 'Min Damage': 10},
                                       'EXP': 0,
                                       'HP': 20, 'Level': 1,
                                       'Level Name': {'Level1': 'python soldier', 'Level2': 'python warrior',
                                                      'Level3': 'python hero'}, 'Name': 'Edward',
                                       'Passive': 'pythonic'}

        self.security_character = {'Class': 'python warrior', 'Damage': {'Max Damage': 12, 'Min Damage': 10},
                                       'EXP': 0,
                                       'HP': 20, 'Level': 1,
                                       'Level Name': {'Level1': 'python soldier', 'Level2': 'python warrior',
                                                      'Level3': 'python hero'}, 'Name': 'Edward',
                                       'Passive': 'security'}
        self.monster = {"Name": "Algorithm", "Passive": None, "Is Boss": False, "HP": 20, "EXP": 4,
                        "Damage": {"Max Damage": 4, "Min Damage": 3}}

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('game.critical_counter', return_value=10)
    def test_attack_character_attack_monster_with_norm_dmg(self, mock_dmg, mock_stdout):
        attack(self.non_security_character, self.monster)
        actual_hp = self.monster["HP"]
        expect_hp = 10
        actual_msg = mock_stdout.getvalue()
        expect_msg = 'Edward did 10 damage to Algorithm\n'
        self.assertEqual(expect_hp, actual_hp)
        self.assertEqual(expect_msg, actual_msg)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('game.critical_counter', return_value=12)
    def test_attack_character_attack_monster_with_critical_dmg(self, mock_dmg, mock_stdout):
        attack(self.non_security_character, self.monster)
        actual_hp = self.monster["HP"]
        expect_hp = 8
        actual_msg = mock_stdout.getvalue()
        expect_msg = 'Edward did critical 12 damage to Algorithm\n'
        self.assertEqual(expect_hp, actual_hp)
        self.assertEqual(expect_msg, actual_msg)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('game.critical_counter', return_value=3)
    def test_attack_monster_attack_non_security_char_with_norm_dmg(self, mock_dmg, mock_stdout):
        attack(self.monster, self.non_security_character)
        actual_hp = self.non_security_character["HP"]
        expect_hp = 17
        actual_msg = mock_stdout.getvalue()
        expect_msg = 'Algorithm did 3 damage to Edward\n'
        self.assertEqual(expect_hp, actual_hp)
        self.assertEqual(expect_msg, actual_msg)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('game.critical_counter', return_value=4)
    def test_attack_monster_attack_non_security_char_with_critical_dmg(self, mock_dmg, mock_stdout):
        attack(self.monster, self.non_security_character)
        actual_hp = self.non_security_character["HP"]
        expect_hp = 16
        actual_msg = mock_stdout.getvalue()
        expect_msg = 'Algorithm did critical 4 damage to Edward\n'
        self.assertEqual(expect_hp, actual_hp)
        self.assertEqual(expect_msg, actual_msg)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('game.damage_dodger', return_value=True)
    @patch('game.critical_counter', return_value=4)
    def test_attack_monster_attack_security_char_with_critical_dmg_and_dodge(self, mock_dmg, mock_dodger, mock_stdout):
        attack(self.monster, self.security_character)
        actual_hp = self.security_character["HP"]
        expect_hp = 18
        actual_msg = mock_stdout.getvalue()
        expect_msg = 'Algorithm did critical 4 damage to Edward\nEdward dodged its damage to 2 using "security"\n'
        self.assertEqual(expect_hp, actual_hp)
        self.assertEqual(expect_msg, actual_msg)