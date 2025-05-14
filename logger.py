import logging

# Configure logging
logging.basicConfig(
    filename='trading_bot.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_error(error_message):
    """Log errors."""
    logging.error(error_message)

def log_info(info_message):
    """Log information."""
    logging.info(info_message)
