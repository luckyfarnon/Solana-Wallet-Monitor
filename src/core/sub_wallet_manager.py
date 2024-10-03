class SubWalletManager:
    def __init__(self):
        self.active_wallets = {}
        self.inactive_wallets = {}

    def add_wallet(self, wallet_address):
        if wallet_address not in self.active_wallets:
            self.active_wallets[wallet_address] = 0  # Initialize balance to 0
            print(f'Wallet added: {wallet_address}')

    def remove_wallet(self, wallet_address):
        if wallet_address in self.active_wallets:
            del self.active_wallets[wallet_address]
            self.inactive_wallets[wallet_address] = 0  # Track removed wallets
            print(f'Wallet removed: {wallet_address}')

    def update_balance(self, wallet_address, amount):
        if wallet_address in self.active_wallets:
            self.active_wallets[wallet_address] += amount
            print(f'Balance updated for {wallet_address}: {self.active_wallets[wallet_address]}')

    def get_active_wallets(self):
        return self.active_wallets.keys()

    def get_inactive_wallets(self):
        return self.inactive_wallets.keys()
