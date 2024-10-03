import asyncio
import random
import json

class TestnetSimulator:
    def __init__(self, data_source):
        self.data_source = data_source

    async def simulate_transactions(self):
        while True:
            transaction = self.generate_random_transaction()
            self.process_transaction(transaction)
            await asyncio.sleep(random.uniform(0.5, 2.0))  # Simulate delay

    def generate_random_transaction(self):
        # Generate a random transaction for testing purposes
        return {
            'token_address': 'TokenAddress_' + str(random.randint(1, 100)),
            'amount': random.uniform(0.1, 10.0)
        }

    def process_transaction(self, transaction):
        # Process the simulated transaction
        print(f"Simulated transaction: {json.dumps(transaction)}")

if __name__ == '__main__':
    simulator = TestnetSimulator(data_source=None)  # Replace with actual data source if needed
    asyncio.run(simulator.simulate_transactions())
