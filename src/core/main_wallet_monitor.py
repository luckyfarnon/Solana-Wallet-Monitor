import asyncio
import websockets
import json
import time
from src.data.data_manager import DataManager
from src.utils.logging_utils import setup_logging

class MainWalletMonitor:
    def __init__(self, uri, db_file):
        self.uri = uri
        self.data_manager = DataManager(db_file)

    async def monitor(self):
        while True:
            try:
                async with websockets.connect(self.uri) as websocket:
                    while True:
                        message = await websocket.recv()
                        self.process_message(message)
            except (websockets.ConnectionClosed, OSError) as e:
                print(f"Connection error: {e}. Reconnecting in 5 seconds...")
                await asyncio.sleep(5)  # Wait before reconnecting

    def process_message(self, message):
        # Process the incoming message and log it
        data = json.loads(message)
        token_address = data.get('token_address')
        amount = data.get('amount')
        if token_address and amount:
            self.data_manager.add_trade(token_address, amount)
            print(f'Trade logged: {token_address} - {amount}')

if __name__ == '__main__':
    uri = "wss://api.mainnet.solana.com"  # Example WebSocket endpoint
    db_file = 'trades.db'
    monitor = MainWalletMonitor(uri, db_file)
    asyncio.run(monitor.monitor())
