import os

# Load API credentials from environment variables
API_KEY = os.getenv('BINANCE_API_KEY')
API_SECRET = os.getenv('BINANCE_API_SECRET')

# Constants for trading
DEFAULT_SYMBOL = "BTCUSDT"
DEFAULT_QUANTITY = 0.01
