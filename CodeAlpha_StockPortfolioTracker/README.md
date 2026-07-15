# CodeAlpha Stock Portfolio Tracker

A simple command-line stock portfolio tracker built in Python as part of the **CodeAlpha Python Programming Internship (Task 2)**.

## 📖 About

The user selects stocks from a predefined list, enters how many shares of each they want to "buy," and the program calculates the total investment value. The summary can optionally be saved to a `.txt` or `.csv` file.

## 🚀 How to Run

1. Make sure Python 3 is installed on your system.
2. Clone this repository:
```bash
   git clone https://github.com/tejaswiniv589-afk/CodeAlpha_StockPortfolioTracker.git
   cd CodeAlpha_StockPortfolioTracker
```
3. Run the script:
```bash
   python portfolio_tracker.py
```

## 🎮 How to Use

1. The program displays a list of available stocks and their prices.
2. Enter a stock symbol (e.g. `AAPL`) and the quantity you want.
3. Repeat for as many stocks as you like.
4. Type `done` when finished.
5. View your portfolio summary, including per-stock value and total investment.
6. Choose whether to save the summary as a `.txt` or `.csv` file.

## 📈 Available Stocks (hardcoded prices)

| Symbol | Price (USD) |
|--------|-------------|
| AAPL   | 180         |
| TSLA   | 250         |
| GOOGL  | 140         |
| AMZN   | 175         |
| MSFT   | 420         |
| META   | 480         |
| NFLX   | 650         |
| NVDA   | 120         |

## 🛠 Concepts Used

- Dictionaries (stock prices, portfolio storage)
- Input/output and input validation
- Basic arithmetic
- File handling (`.txt` and `.csv` export)
- Functions and loops

## 📌 Internship

This project was completed as part of the **Python Programming Internship** at [CodeAlpha](https://www.codealpha.tech).
