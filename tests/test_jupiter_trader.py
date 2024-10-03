# test_jupiter_trader.py

import unittest
import sys
import os
from core.jupiter_trader import JupiterTrader

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

class TestJupiterTrader(unittest.TestCase):
    def setUp(self):
        self.trader = JupiterTrader()

    def test_execute_trade(self):
        response = self.trader.execute_trade('token_address', 100)
        self.assertIsNotNone(response)  # Placeholder for actual response validation

    def test_get_trade_history(self):
        history = self.trader.get_trade_history()
        self.assertIsInstance(history, list)  # Placeholder for actual response validation

if __name__ == '__main__':
    unittest.main()

