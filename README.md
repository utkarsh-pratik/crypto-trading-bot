# Binance Testnet Trading Bot

This is a Python-based simplified trading bot that interacts with the Binance Futures Testnet API. It supports placing market, limit, and stop-limit orders with both buy and sell sides.

## Prerequisites
1. **Python 3.7 or higher**.
2. Install dependencies:
    ```bash
    pip install python-binance
    pip install requests logging
    ```

3. Register a Binance Testnet account at [Binance Futures Testnet](https://testnet.binancefuture.com) and generate API credentials.

## Files
- `bot.py`: Core trading bot logic.
- `config.py`: Configuration and API credentials.
- `logger.py`: Logging functionality.
- `cli_interface.py`: Command-line interface for user interaction.

## Setup
1. Clone the repository:
    ```bash
    git clone <repo_url>
    cd trading_bot
    ```

2. Export API credentials as environment variables:
    ```bash
    export BINANCE_API_KEY="your_api_key"
    export BINANCE_API_SECRET="your_api_secret"
    ```

3. Run the CLI:
    ```bash
    python cli_interface.py
    ```

## Features
- Place **Market Orders**.
- Place **Limit Orders**.
- Place **Stop-Limit Orders**.
- Supports both **Buy** and **Sell** sides.
- Logs all API requests, responses, and errors to `trading_bot.log`.

## Testing
- Test various order types and parameters on the Binance Futures Testnet.
- Check `trading_bot.log` for detailed logs of each API request and response.

## Notes
- This bot is for educational purposes and runs on the Binance Futures Testnet (paper trading).
- Do not use this bot for live trading without proper risk management.
