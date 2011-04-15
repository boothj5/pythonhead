from game import Game
import unittest

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game(2,3,["James", "Mark"])    
    
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
