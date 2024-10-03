# test_token_detector.py

import unittest
from core.token_detector import TokenDetector
from core.sub_wallet_manager import SubWalletManager

class TestTokenDetector(unittest.TestCase):
    def setUp(self):
        self.sub_wallet_manager = SubWalletManager()
        self.token_detector = TokenDetector(self.sub_wallet_manager)

    def test_detect_new_token(self):
        self.token_detector.detect_new_token('token1')
        self.assertIn('token1', self.token_detector.detected_tokens)

    def test_detect_existing_token(self):
        self.token_detector.detect_new_token('token2')
        self.token_detector.detect_new_token('token2')  # Should not add again
        self.assertEqual(len(self.token_detector.detected_tokens), 1)

if __name__ == '__main__':
    unittest.main()
