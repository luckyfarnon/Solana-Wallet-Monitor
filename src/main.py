import asyncio
import logging
from utils.logging_utils import logger

async def main():
    logger.info('Starting Solana Wallet Monitor and Trader...')
    
    try:
        logger.info('Entering main loop...')
        
        for i in range(5):  # Run for a limited number of iterations
            logger.debug(f'Main loop iteration {i + 1}...')
            # Simulate some processing
            await asyncio.sleep(1)  # Replace with actual logic
            logger.debug('Completed processing for this iteration.')

    except asyncio.CancelledError:
        logger.info('Main loop was cancelled.')
    except Exception as e:
        logger.error(f'An error occurred: {e}')

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info('Program was interrupted by user.')
