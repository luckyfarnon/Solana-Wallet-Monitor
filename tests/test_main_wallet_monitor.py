# test_main_wallet_monitor.py

import unittest
import sys
import os
from core.main_wallet_monitor import MainWalletMonitor

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

class TestMainWalletMonitor(unittest.TestCase):
    def setUp(self):
        self.monitor = MainWalletMonitor()

    def test_initialization(self):
        self.assertIsNotNone(self.monitor)

    # Additional tests can be added here

if __name__ == '__main__':
    unittest.main()

