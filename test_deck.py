from deck import Deck
from card import Card
import unittest

class TestDeck(unittest.TestCase):

    def setUp(self):
        self.deck = Deck(52)
    
    def test_create_0_cards(self):
        deck = Deck(0)
        self.assertEqual(len(deck), 0)

    def test_create_20_cards(self):
        deck = Deck(20)
        self.assertEqual(len(deck), 52)
    
    def test_create_51_cards(self):
        deck = Deck(51)
        self.assertEqual(len(deck), 52)

    def test_create_52_cards(self):
        deck = Deck(52)
        self.assertEqual(len(deck), 52)
        
    def test_create_53_cards(self):
        deck = Deck(53)
        self.assertEqual(len(deck), 104)

    def test_create_103_cards(self):
        deck = Deck(103)
        self.assertEqual(len(deck), 104)

    def test_create_104_cards(self):
        deck = Deck(104)
        self.assertEqual(len(deck), 104)

    def test_create_105_cards(self):
        deck = Deck(105)
        self.assertEqual(len(deck), 156)

    def test_create_200_cards(self):
        deck = Deck(200)
        self.assertEqual(len(deck), 208)

    def test_pop_none_from_empty_deck_returns_empty_list(self):
        deck = Deck(0)
        result = deck.pop_card(0)
        self.assertEqual([], result)

    def test_pop_one_from_empty_deck_returns_empty_list(self):
        deck = Deck(0)
        result = deck.pop_card()
        self.assertEqual([], result)

    def test_pop_five_from_empty_deck_returns_empty_list(self):
        deck = Deck(0)
        result = deck.pop_card(5)
        self.assertEqual([], result)

    def test_pop_one_from_deck_returns_one(self):
        result = self.deck.pop_card(1)
        self.assertEqual([Card(14,4)], result)

    def test_pop_one_from_deck_leaves_51(self):
        result = self.deck.pop_card(1)
        self.assertEqual([Card(14,4)], result)

    def test_pop_one_from_deck(self):
        card = self.deck.pop_card()[0]
        remaining_length = len(self.deck)
        still_in_deck = False
        for i in range(51):
            test_card = self.deck.pop_card()[0]
            if test_card == card:
                still_in_deck = True
                break
        self.assertEqual(remaining_length, 51)
        self.assertFalse(still_in_deck)


    def test_pop_three_from_deck(self):
        cards = self.deck.pop_card(3)
        remaining_length = len(self.deck)
        still_in_deck = False
        for i in range(49):
            test_card = self.deck.pop_card()[0]
            if test_card in cards:
                still_in_deck = True
                break
        self.assertEqual(remaining_length, 49)
        self.assertFalse(still_in_deck)



