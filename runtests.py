import unittest
from cardtest import TestCard
from playertest import TestPlayer

suite = unittest.TestLoader().loadTestsFromTestCase(TestCard)
unittest.TextTestRunner(verbosity=2).run(suite)

suite = unittest.TestLoader().loadTestsFromTestCase(TestPlayer)
unittest.TextTestRunner(verbosity=2).run(suite)
