from bot import BasicBot
from config import API_KEY, API_SECRET, DEFAULT_SYMBOL, DEFAULT_QUANTITY

def main():
    """Main command-line interface for the bot."""
    print("Welcome to the Binance Testnet Trading Bot!")
    
    # Initialize the bot
    bot = BasicBot(API_KEY, API_SECRET, testnet=True)

    while True:
        # Get user input
        order_type = input("Order Type (market/limit/stop-limit): ").strip().lower()
        side = input("Order Side (buy/sell): ").strip().upper()
        symbol = input(f"Symbol (default: {DEFAULT_SYMBOL}): ").strip().upper() or DEFAULT_SYMBOL
        quantity = float(input(f"Quantity (default: {DEFAULT_QUANTITY}): ") or DEFAULT_QUANTITY)

        if order_type == "market":
            # Place market order
            result = bot.place_market_order(symbol, side, quantity)
        elif order_type == "limit":
            # Ask for limit price
            price = float(input("Limit Price: "))
            result = bot.place_limit_order(symbol, side, quantity, price)
        elif order_type == "stop-limit":
            # Ask for stop price and limit price
            stop_price = float(input("Stop Price: "))
            limit_price = float(input("Limit Price: "))
            result = bot.place_stop_limit_order(symbol, side, quantity, stop_price, limit_price)
        else:
            print("Invalid order type. Please try again.")
            continue

        # Output order details
        if result:
            print("Order successful!")
            print(result)
        else:
            print("Order failed. Check logs for more details.")

        # Exit or continue
        cont = input("Do you want to place another order? (yes/no): ").strip().lower()
        if cont != 'yes':
            break

if __name__ == "__main__":
    main()
