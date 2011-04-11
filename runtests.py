import unittest
from cardtest import TestCard
from playertest import TestPlayer
from decktest import TestDeck

suite = unittest.TestLoader().loadTestsFromTestCase(TestCard)
unittest.TextTestRunner(verbosity=0).run(suite)

suite = unittest.TestLoader().loadTestsFromTestCase(TestDeck)
unittest.TextTestRunner(verbosity=0).run(suite)

suite = unittest.TestLoader().loadTestsFromTestCase(TestPlayer)
unittest.TextTestRunner(verbosity=0).run(suite)