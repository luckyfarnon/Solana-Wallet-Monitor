# sub_wallet_manager.py

from utils.logging_utils import logger

class SubWalletManager:
    def __init__(self):
        self.active_wallets = {}

    def add_wallet(self, wallet_address):
        if wallet_address not in self.active_wallets:
            self.active_wallets[wallet_address] = {'balance': 0}
            logger.info(f'Added new wallet: {wallet_address}')
        else:
            logger.info(f'Wallet already exists: {wallet_address}')

    def remove_wallet(self, wallet_address):
        if wallet_address in self.active_wallets:
            del self.active_wallets[wallet_address]
            logger.info(f'Removed wallet: {wallet_address}')
        else:
            logger.warning(f'Attempted to remove non-existing wallet: {wallet_address}')

    def update_balance(self, wallet_address, balance):
        if wallet_address in self.active_wallets:
            self.active_wallets[wallet_address]['balance'] = balance
            logger.info(f'Updated balance for {wallet_address}: {balance}')
        else:
            logger.warning(f'Attempted to update balance for non-existing wallet: {wallet_address}')

    def get_active_wallets(self):
        return self.active_wallets
