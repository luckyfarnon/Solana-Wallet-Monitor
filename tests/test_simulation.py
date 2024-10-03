import unittest
import sys
import os
import asyncio
from unittest.mock import patch, AsyncMock
from simulation.mainnet_replicator import MainnetReplicator
from data.data_manager import DataManager

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

class TestMainnetReplicator(unittest.TestCase):
    def setUp(self):
        self.data_manager = DataManager('data/solana_wallet_monitor.db')
        self.replicator = MainnetReplicator(uri='wss://api.mainnet.solana.com')

    @patch('websockets.connect', new_callable=AsyncMock)
    def test_replicate_data(self, mock_connect):
        mock_websocket = AsyncMock()
        mock_connect.return_value.__aenter__.return_value = mock_websocket
        mock_connect.return_value.__aexit__.return_value = False  # Simulate exiting context manager
        
        # Simulate receiving data
        mock_websocket.recv.side_effect = [b'{"data": "test"}', asyncio.CancelledError()]
        
        # Await the coroutine properly
        asyncio.run(self.replicator.replicate_data())

if __name__ == '__main__':
    unittest.main()
