# cli.py

import argparse
from core.main_wallet_monitor import main_wallet_monitor_loop
from core.sub_wallet_manager import SubWalletManager
from core.token_detector import TokenDetector
from core.jupiter_trader import JupiterTrader
from data.data_manager import DataManager
from utils.logging_utils import logger

def main():
    parser = argparse.ArgumentParser(description='Solana Wallet Monitor and Trader CLI')
    parser.add_argument('--start', action='store_true', help='Start the wallet monitor')
    args = parser.parse_args()

    if args.start:
        logger.info('Starting Solana Wallet Monitor')
        # Initialize components
        data_manager = DataManager('data/solana_wallet_monitor.db')
        sub_wallet_manager = SubWalletManager()
        token_detector = TokenDetector(sub_wallet_manager)
        jupiter_trader = JupiterTrader()
        # Start the main wallet monitor loop
        main_wallet_monitor_loop()

if __name__ == '__main__':
    main()
