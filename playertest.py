from player import Player
from card import Card
import unittest

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.james = Player("James")
        self.two = Card(2, 1)
        self.three = Card(3, 1)
        self.four = Card(4, 1)
        self.five = Card(5, 1)
        self.six = Card(6, 1)
        self.seven = Card(7, 1)
        self.eight = Card(8, 1)
        self.nine = Card(9, 1)
        self.ten = Card(10, 1)
        self.jack = Card(11, 1)
        self.queen = Card(12, 1)
        self.king = Card(13, 1)
        self.ace = Card(14, 1)

    def test_player_not_has_hand(self):
        self.assertFalse(self.james.has_hand())

    def test_player_has_hand_one_card(self):
        self.james.hand.append(self.two)
        self.assertTrue(self.james.has_hand())

    def test_player_has_hand_two_cards(self):
        self.james.hand.extend([self.two, self.ace])
        self.assertTrue(self.james.has_hand())

    def test_player_not_has_faceup(self):
        self.assertFalse(self.james.has_faceup())

    def test_player_has_faceup_one_card(self):
        self.james.faceup.append(self.seven)
        self.assertTrue(self.james.has_faceup())

    def test_player_has_faceup_two_cards(self):
        self.james.faceup.extend([self.nine, self.three])
        self.assertTrue(self.james.has_faceup())

    def test_recieve_none(self):
        self.james.hand.append(self.ten)
        self.james.receive([])
        expected_result = [self.ten]
        self.assertEqual(self.james.hand, expected_result)
        
    def test_recieve_one_when_empty(self):
        self.james.receive([self.jack])
        expected_result = [self.jack]
        self.assertEqual(self.james.hand, expected_result)

    def test_recieve_one_when_three(self):
        self.james.hand.extend([self.jack, self.nine, self.ace])
        self.james.receive([self.two])
        receieved = self.jack in self.james.hand and \
                    self.nine in self.james.hand and \
                    self.ace in self.james.hand and \
                    self.two in self.james.hand
        self.assertTrue(receieved)

