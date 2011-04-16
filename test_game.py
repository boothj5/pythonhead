from game import Game
from card import Card

import unittest

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game(2,3,["James", "Mark"])    
        self.two = Card(2, 1)
        self.three1 = Card(3, 1)
        self.three2 = Card(3, 2)
        self.three3 = Card(3, 3)
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
    
    def test_deal(self):
        self.game.deal()
        hands_dealt = reduce(lambda acc, p : len(p.hand) == 3 and acc, self.game.players, True)
        ups_dealt = reduce(lambda acc, p : len(p.faceup) == 3 and acc, self.game.players, True)
        downs_dealt = reduce(lambda acc, p : len(p.facedown) == 3 and acc, self.game.players, True)
        removed_from_deck = len(self.game.deck) == 52 - 18
        self.assertTrue(hands_dealt)
        self.assertTrue(ups_dealt)
        self.assertTrue(downs_dealt)
        self.assertTrue(removed_from_deck)

    def test_first_move_one_card(self):
        self.game.players[0].hand = [self.two, self.eight, self.ace]
        self.game.players[1].hand = [self.five, self.nine, self.ten]
        self.game.first_move()
        card_dealt_from_deck = len(self.game.deck) == 51
        card_dealt_to_player = len(self.game.players[1].hand) == 3
        correct_card_laid = self.game.pile.pop() == self.five
        moved_to_next = self.game.turn == 0
        self.assertTrue(card_dealt_from_deck)
        self.assertTrue(card_dealt_to_player)
        self.assertTrue(correct_card_laid)
        self.assertTrue(moved_to_next)
        
    def test_first_move_three_cards(self):
        self.game.players[0].hand = [self.three1, self.three2, self.three3, self.two]
        self.game.players[1].hand = [self.five, self.nine, self.ten, self.eight]
        self.game.first_move()
        card_dealt_from_deck = len(self.game.deck) == 49
        card_dealt_to_player = len(self.game.players[0].hand) == 4
        cards_laid = []
        cards_laid.append(self.game.pile.pop())
        cards_laid.append(self.game.pile.pop())
        cards_laid.append(self.game.pile.pop())
        correct_cards_laid = self.three1 in cards_laid and \
                             self.three2 in cards_laid and \
                             self.three3 in cards_laid
        moved_to_next = self.game.turn == 1
        self.assertTrue(card_dealt_from_deck)
        self.assertTrue(card_dealt_to_player)
        self.assertTrue(correct_cards_laid)
        self.assertTrue(moved_to_next)
