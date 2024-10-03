import unittest
import sys
import os
from core.sub_wallet_manager import SubWalletManager

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

class TestSubWalletManager(unittest.TestCase):
    def setUp(self):
        self.manager = SubWalletManager()

    def test_update_balance(self):
        self.manager.add_wallet('wallet3')
        self.manager.update_balance('wallet3', 100)  # Corrected to include comma
        self.assertEqual(self.manager.active_wallets['wallet3'], 100)  # Corrected to access balance directly

if __name__ == '__main__':
    unittest.main()
