import argparse
from src.data.data_manager import DataManager
from src.utils.logging_utils import setup_logging

def main():
    setup_logging()
    parser = argparse.ArgumentParser(description='Solana Wallet Monitor and Trader CLI')
    parser.add_argument('--token', type=str, required=True, help='Token address to monitor')
    parser.add_argument('--amount', type=float, required=True, help='Amount of token to trade')
    args = parser.parse_args()

    data_manager = DataManager(db_file='trades.db')  # Specify your database file
    data_manager.add_trade(args.token, args.amount)
    print(f'Trade added: {args.token} - {args.amount}')
    data_manager.close()

if __name__ == '__main__':
    main()
