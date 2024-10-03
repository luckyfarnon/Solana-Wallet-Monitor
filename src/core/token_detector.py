# token_detector.py

from utils.logging_utils import logger

class TokenDetector:
    def __init__(self, sub_wallet_manager):
        self.sub_wallet_manager = sub_wallet_manager
        self.detected_tokens = set()

    def detect_new_token(self, token_address):
        if token_address not in self.detected_tokens:
            self.detected_tokens.add(token_address)
            logger.info(f'Detected new token: {token_address}')
            # Placeholder for further processing (e.g., retrieving token metadata)
            try:
                # Simulate token metadata retrieval
                metadata = self.retrieve_token_metadata(token_address)
                logger.info(f'Retrieved metadata for token: {metadata}')
            except Exception as e:
                logger.error(f'Error retrieving metadata for token {token_address}: {e}')
        else:
            logger.info(f'Token already detected: {token_address}')

    def retrieve_token_metadata(self, token_address):
        # Placeholder for actual metadata retrieval logic
        # Simulating a potential error
        if token_address == 'invalid_token':
            raise ValueError('Invalid token address')
        return {'name': 'Sample Token', 'symbol': 'STK'}

    def get_detected_tokens(self):
        return list(self.detected_tokens)

