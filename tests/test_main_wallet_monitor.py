import unittest
import asyncio
import sys
import os
from core.main_wallet_monitor import MainWalletMonitor

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

class TestMainWalletMonitor(unittest.TestCase):
    def setUp(self):
        self.monitor = MainWalletMonitor(uri='wss://api.mainnet.solana.com', db_file='data/solana_wallet_monitor.db')

    def test_initialization(self):
        self.assertIsNotNone(self.monitor)

    def test_connection_stability(self):
        # This test would require mocking the WebSocket connection to simulate connection drops
        pass  # Implementation of this test would go here

if __name__ == '__main__':
    unittest.main()
