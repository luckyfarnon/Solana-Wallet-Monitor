import unittest
import sys
import os
from unittest.mock import patch, Mock
from core.jupiter_trader import JupiterTrader

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

class TestJupiterTrader(unittest.TestCase):
    def setUp(self):
        self.trader = JupiterTrader(api_url='http://mockapi.com')  # Updated to a mock API URL

    @patch('requests.post')  # Mock the requests.post method
    def test_execute_trade(self, mock_post):
        # Mock the response from the API
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'success': True, 'trade_id': '12345'}
        mock_post.return_value = mock_response

        response = self.trader.execute_trade('token_address', 100)
        self.assertIsNotNone(response)  # Check that response is not None
        self.assertEqual(response['success'], True)  # Check for success in response

    def test_get_trade_history(self):
        history = self.trader.get_trade_history()
        self.assertIsInstance(history, list)  # Placeholder for actual response validation

if __name__ == '__main__':
    unittest.main()
