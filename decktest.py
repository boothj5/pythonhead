from deck import Deck
import unittest

class TestDeck(unittest.TestCase):

    def setUp(self):
        pass
    
    def test_create_52_cards(self):
        deck = Deck(52)
        self.assertEqual(len(deck), 52)