import unittest
from test_card import TestCard
from test_player import TestPlayer
from test_deck import TestDeck

test_cases = ["test_card",
              "test_player",
              "test_deck"]

suite = unittest.TestLoader().loadTestsFromNames(test_cases)
unittest.TextTestRunner(verbosity=0).run(suite)
