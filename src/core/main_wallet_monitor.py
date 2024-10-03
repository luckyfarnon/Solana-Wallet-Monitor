# main_wallet_monitor.py

import asyncio
import websockets
import json
from utils.logging_utils import logger
from config.settings import settings

class MainWalletMonitor:
    def __init__(self):
        self.websocket_url = settings.SOLANA_RPC_URL.replace('http', 'ws')

    async def connect(self):
        async with websockets.connect(self.websocket_url) as websocket:
            logger.info('Connected to Solana WebSocket')
            await self.listen(websocket)

    async def listen(self, websocket):
        try:
            while True:
                message = await websocket.recv()
                data = json.loads(message)
                logger.info(f'Received data: {data}')
                # Placeholder for parsing and filtering logic
        except websockets.ConnectionClosed as e:
            logger.error(f'WebSocket connection closed: {e}')
        except Exception as e:
            logger.error(f'Error in WebSocket listener: {e}')

async def main_wallet_monitor_loop():
    monitor = MainWalletMonitor()
    await monitor.connect()

if __name__ == '__main__':
    try:
        asyncio.run(main_wallet_monitor_loop())
    except KeyboardInterrupt:
        logger.info('Main wallet monitor interrupted by user')
