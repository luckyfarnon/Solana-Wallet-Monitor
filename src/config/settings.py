# settings.py

import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    SOLANA_RPC_URL = os.getenv('SOLANA_RPC_URL', 'https://api.mainnet-beta.solana.com')
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///data/solana_wallet_monitor.db')
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')

settings = Settings()
