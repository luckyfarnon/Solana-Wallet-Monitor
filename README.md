# Solana Wallet Monitor and Trader

## Overview
The Solana Wallet Monitor and Trader is a comprehensive application designed to monitor wallet transactions on the Solana blockchain and facilitate trading through the Jupiter API. This project provides real-time updates on wallet activities and allows users to execute trades based on detected tokens.

## Features
- **Real-time Wallet Monitoring**: Connects to the Solana network via WebSocket to monitor transactions.
- **Dynamic Sub-Wallet Management**: Supports tracking of multiple sub-wallets and their respective balances.
- **Token Detection**: Automatically detects new tokens in monitored wallets and logs relevant information.
- **Trading Integration**: Executes trades through the Jupiter API based on detected tokens.
- **Data Persistence**: Stores transaction history and logs in a SQLite database.
- **User Interface**: Provides a command-line interface for user interaction.
- **Error Handling**: Implements robust error handling and logging mechanisms.

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd solana-wallet-monitor-trader
   ```
2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure environment variables in the `.env` file.

## Usage
To start monitoring a wallet, use the command-line interface:
```bash
python src/ui/cli.py --token <TOKEN_ADDRESS> --amount <AMOUNT>
```

## Testing
Run the unit tests to ensure functionality:
```bash
pytest tests/
```

## Documentation
Refer to the `docs/` directory for detailed documentation on setup, usage, and API reference.

## License
This project is licensed under the MIT License.

## Acknowledgments
- Solana Blockchain
- Jupiter API
- SQLite
- Python

## Conclusion
The Solana Wallet Monitor and Trader project provides a robust solution for monitoring and trading on the Solana blockchain, with potential for future enhancements.