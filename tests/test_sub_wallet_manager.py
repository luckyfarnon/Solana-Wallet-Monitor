# test_sub_wallet_manager.py

import unittest
import sys
import os
from core.sub_wallet_manager import SubWalletManager

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

class TestSubWalletManager(unittest.TestCase):
    def setUp(self):
        self.manager = SubWalletManager()

    def test_add_wallet(self):
        self.manager.add_wallet('wallet1')
        self.assertIn('wallet1', self.manager.active_wallets)

    def test_remove_wallet(self):
        self.manager.add_wallet('wallet2')
        self.manager.remove_wallet('wallet2')
        self.assertNotIn('wallet2', self.manager.active_wallets)

    def test_update_balance(self):
        self.manager.add_wallet('wallet3')
        self.manager.update_balance('wallet3', 100)
        self.assertEqual(self.manager.active_wallets['wallet3']['balance'], 100)

if __name__ == '__main__':
    unittest.main()

