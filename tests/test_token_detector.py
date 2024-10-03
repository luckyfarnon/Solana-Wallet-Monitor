import unittest
import sys
import os
from core.token_detector import TokenDetector
from core.sub_wallet_manager import SubWalletManager

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

class TestTokenDetector(unittest.TestCase):
    def setUp(self):
        self.sub_wallet_manager = SubWalletManager()
        self.token_detector = TokenDetector(self.sub_wallet_manager)

    def test_detect_new_token(self):
        self.token_detector.detect_token('token1', metadata={'name': 'Token One'})
        self.assertIn('token1', self.token_detector.detected_tokens)

    def test_detect_existing_token(self):
        self.token_detector.detect_token('token2', metadata={'name': 'Token Two'})
        self.token_detector.detect_token('token2', metadata={'name': 'Token Two'})  # Should not add again
        self.assertEqual(len(self.token_detector.detected_tokens), 1)

if __name__ == '__main__':
    unittest.main()
