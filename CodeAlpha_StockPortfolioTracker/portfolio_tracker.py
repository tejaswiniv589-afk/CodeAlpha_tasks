"""
Stock Portfolio Tracker
CodeAlpha Python Programming Internship - Task 2

Lets the user build a small portfolio by entering stock names and
quantities. Prices come from a hardcoded dictionary. Calculates the
total investment value and optionally saves a summary to a file.
"""

import csv
from datetime import datetime

# Hardcoded stock prices (in USD)
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 175,
    "MSFT": 420,
    "META": 480,
    "NFLX": 650,
    "NVDA": 120,
}


def show_available_stocks():
    """Print the list of stocks the user can invest in, with prices."""
    print("\nAvailable Stocks:")
    print("-" * 30)
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol:<8} ${price}")
    print("-" * 30)


def get_portfolio_input():
    """
    Repeatedly ask the user for a stock symbol and quantity.
    Returns a dictionary of {symbol: quantity}.
    """
    portfolio = {}

    print("\nEnter stock symbol and quantity (type 'done' to finish).")

    while True:
        symbol = input("\nStock symbol (e.g. AAPL): ").upper().strip()

        if symbol == "DONE":
            break

        if symbol not in STOCK_PRICES:
            print(f"'{symbol}' is not in the available stock list. Please try again.")
            continue

        # Keep asking for quantity until a valid positive whole number is given
        while True:
            qty_input = input(f"Quantity of {symbol}: ").strip()

            if not qty_input.isdigit() or int(qty_input) <= 0:
                print("Please enter a valid positive whole number for quantity.")
                continue

            quantity = int(qty_input)
            break

        # If the stock is already added, increase the quantity instead of overwriting
        portfolio[symbol] = portfolio.get(symbol, 0) + quantity
        print(f"Added {quantity} share(s) of {symbol}.")

    return portfolio


def calculate_investment(portfolio):
    """
    Given a {symbol: quantity} dictionary, return a list of
    (symbol, quantity, price, value) tuples and the total value.
    """
    breakdown = []
    total = 0

    for symbol, quantity in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * quantity
        breakdown.append((symbol, quantity, price, value))
        total += value

    return breakdown, total


def display_summary(breakdown, total):
    """Print a formatted investment summary to the console."""
    print("\n" + "=" * 45)
    print("PORTFOLIO SUMMARY")
    print("=" * 45)
    print(f"{'Stock':<8}{'Qty':<8}{'Price':<10}{'Value':<10}")
    print("-" * 45)

    for symbol, quantity, price, value in breakdown:
        print(f"{symbol:<8}{quantity:<8}${price:<9}${value:<9}")

    print("-" * 45)
    print(f"{'TOTAL INVESTMENT:':<26}${total}")
    print("=" * 45)


def save_to_file(breakdown, total, file_format="txt"):
    """Save the portfolio summary to a .txt or .csv file."""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    if file_format == "csv":
        filename = f"portfolio_summary_{timestamp}.csv"
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Stock", "Quantity", "Price", "Value"])
            for symbol, quantity, price, value in breakdown:
                writer.writerow([symbol, quantity, price, value])
            writer.writerow([])
            writer.writerow(["Total Investment", "", "", total])
    else:
        filename = f"portfolio_summary_{timestamp}.txt"
        with open(filename, "w") as f:
            f.write("PORTFOLIO SUMMARY\n")
            f.write("=" * 45 + "\n")
            f.write(f"{'Stock':<8}{'Qty':<8}{'Price':<10}{'Value':<10}\n")
            f.write("-" * 45 + "\n")
            for symbol, quantity, price, value in breakdown:
                f.write(f"{symbol:<8}{quantity:<8}${price:<9}${value:<9}\n")
            f.write("-" * 45 + "\n")
            f.write(f"{'TOTAL INVESTMENT:':<26}${total}\n")

    print(f"\nSummary saved to: {filename}")


def main():
    print("=" * 45)
    print("Welcome to the Stock Portfolio Tracker")
    print("=" * 45)

    show_available_stocks()
    portfolio = get_portfolio_input()

    if not portfolio:
        print("\nNo stocks were added. Exiting.")
        return

    breakdown, total = calculate_investment(portfolio)
    display_summary(breakdown, total)

    save_choice = input("\nSave this summary to a file? (y/n): ").lower().strip()
    if save_choice == "y":
        format_choice = input("Choose format - txt or csv: ").lower().strip()
        file_format = "csv" if format_choice == "csv" else "txt"
        save_to_file(breakdown, total, file_format)

    print("\nThank you for using the Stock Portfolio Tracker!")


if __name__ == "__main__":
    main()