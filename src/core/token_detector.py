class TokenDetector:
    def __init__(self, sub_wallet_manager):  # Accept SubWalletManager instance
        self.sub_wallet_manager = sub_wallet_manager
        self.detected_tokens = {}  # Changed to a dictionary to store metadata

    def detect_token(self, token_address, metadata=None):
        if token_address not in self.detected_tokens:
            self.detected_tokens[token_address] = metadata
            print(f'Token detected: {token_address} with metadata: {metadata}')

    def get_detected_tokens(self):
        return list(self.detected_tokens.keys())
