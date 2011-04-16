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
        hands_dealt = reduce(lambda acc, p : len(p.hand) == 3 and acc,
                             self.game.players, True)
        ups_dealt = reduce(lambda acc, p : len(p.faceup) == 3 and acc,
                           self.game.players, True)
        downs_dealt = reduce(lambda acc, p : len(p.facedown) == 3 and acc,
                             self.game.players, True)
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
        card_no_longer_in_hand = self.five not in self.game.players[1].hand
        moved_to_next = self.game.turn == 0
        self.assertTrue(card_dealt_from_deck)
        self.assertTrue(card_no_longer_in_hand)
        self.assertTrue(card_dealt_to_player)
        self.assertTrue(correct_card_laid)
        self.assertTrue(moved_to_next)
        
    def test_first_move_three_cards(self):
        self.game.players[0].hand = [self.three1,
                                     self.three2,
                                     self.three3,
                                     self.two]
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
        cards_no_longer_in_hand = self.three1 not in self.game.players[0].hand and \
                                  self.three2 not in self.game.players[0].hand and \
                                  self.three3 not in self.game.players[0].hand
        moved_to_next = self.game.turn == 1
        self.assertTrue(card_dealt_from_deck)
        self.assertTrue(card_dealt_to_player)
        self.assertTrue(correct_cards_laid)
        self.assertTrue(moved_to_next)

    def test_lay_one_card(self):
        self.game.players[0].hand = [self.five, self.nine, self.ten, self.eight]
        self.game.lay_cards([self.nine])
        card_dealt_from_deck = len(self.game.deck) == 51
        card_dealt_to_player = len(self.game.players[0].hand) == 4
        correct_card_laid = self.game.pile.pop() == self.nine
        card_no_longer_in_hand = self.nine not in self.game.players[0].hand
        self.assertTrue(card_dealt_from_deck)
        self.assertTrue(card_dealt_to_player)
        self.assertTrue(correct_card_laid)
        self.assertTrue(card_no_longer_in_hand)
        
        
    def test_lay_three_cards(self):
        self.game.players[1].hand = [self.five, self.three2, self.three1, self.three3]
        self.game.turn = 1
        self.game.lay_cards([self.three1, self.three3, self.three2])
        card_dealt_from_deck = len(self.game.deck) == 49
        card_dealt_to_player = len(self.game.players[1].hand) == 4
        cards_laid = []
        cards_laid.append(self.game.pile.pop())
        cards_laid.append(self.game.pile.pop())
        cards_laid.append(self.game.pile.pop())
        correct_cards_laid = self.three1 in cards_laid and \
                             self.three2 in cards_laid and \
                             self.three3 in cards_laid
        cards_no_longer_in_hand = self.three1 not in self.game.players[1].hand and \
                                  self.three2 not in self.game.players[1].hand and \
                                  self.three3 not in self.game.players[1].hand
        self.assertTrue(card_dealt_from_deck)
        self.assertTrue(card_dealt_to_player)
        self.assertTrue(correct_cards_laid)
        self.assertTrue(cards_no_longer_in_hand)
        
    def test_first_current_player(self):
        player = self.game.current_player()
        self.assertEquals(player.name, "James")
                        
    def test_second_current_player(self):
        self.game.turn = 1
        player = self.game.current_player()
        self.assertEquals(player.name, "Mark")

    def test_can_lay_three_on_empty(self):
        self.assertTrue(self.game.valid_move([self.three1]))
        
    def test_can_lay_threes_on_empty(self):
        self.assertTrue(self.game.valid_move([self.three1, self.three2, self.three3]))
        
    def test_cannot_lay_different_cards(self):
        self.assertFalse(self.game.valid_move([self.ace, self.ten]))
        
    def test_can_lay_same_rank(self):
        self.game.pile.append(self.three1)
        self.assertTrue(self.game.valid_move([self.three2]))
        
    def test_can_lay_five_on_four(self):
        self.game.pile.append(self.four)
        self.assertTrue(self.game.valid_move([self.four]))

    def test_can_lay_two_on_three(self):
        self.game.pile.append(self.three1)
        self.assertTrue(self.game.valid_move([self.two]))

    def test_can_lay_seven_on_nine(self):
        self.game.pile.append(self.nine)
        self.assertTrue(self.game.valid_move([self.seven]))

    def test_can_lay_ten_on_queen(self):
        self.game.pile.append(self.queen)
        self.assertTrue(self.game.valid_move([self.ten]))

    def test_can_lay_seven_invisible(self):
        self.game.pile.extend([self.three1, self.seven])
        self.assertTrue(self.game.valid_move([self.four]))

    def test_can_play_when_playable_cards_in_hand(self):
        self.game.pile.extend([self.three1, self.ace])
        self.game.players[0].hand = [self.seven]
        self.game.players[0].faceup = [self.four]
        self.assertTrue(self.game.can_play())
        
    def test_cannot_play_when_nonplayable_cards_in_hand(self):
        self.game.pile.extend([self.three1, self.ace])
        self.game.players[0].hand = [self.king]
        self.game.players[0].faceup = [self.four]
        self.assertFalse(self.game.can_play())
        
    def test_can_play_when_playable_cards_in_faceup(self):
        self.game.pile.extend([self.three1, self.ace])
        self.game.players[0].hand = []
        self.game.players[0].faceup = [self.nine, self.ace]
        self.assertTrue(self.game.can_play())
        
    def test_cannot_play_when_nonplayable_cards_in_faceup(self):
        self.game.pile.extend([self.three1, self.ace])
        self.game.players[0].hand = []
        self.game.players[0].faceup = [self.four, self.king]
        self.assertFalse(self.game.can_play())
        
    def test_move_to_next_player(self):
        self.game.next_turn()
        self.assertEquals(self.game.turn, 1)
        
    def test_move_to_next_player_rolls(self):
        self.game.next_turn()
        self.game.next_turn()
        self.assertEquals(self.game.turn, 0)
        
    def test_lowest_player(self):
        self.game.players[0].hand = [self.seven, self.ten]
        self.game.players[1].hand = [self.nine]
        player = self.game.lowest_player()
        self.assertEquals(player.name, "Mark")