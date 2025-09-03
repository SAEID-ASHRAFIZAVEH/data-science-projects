markdown# Stock Price Analyzer

A Python tool that analyzes stock price data using Yahoo Finance API.

## Features
- Fetches real-time stock data for any stock symbol
- Calculates 30-day high, low, and average prices
- Shows price change percentage
- Simple command-line interface

## What I Learned
- Working with financial APIs (yfinance)
- Data manipulation with pandas
- Handling data type conversions
- String formatting in Python

## Installation
```bash
pip install yfinance pandas
Usage
bashpython stock_analyzer.py
Sample Output
📈 Stock Analysis for AAPL
Current Price: $175.25
30-Day High: $182.50
30-Day Low: $165.30
Average Price: $173.80
30-Day Change: +2.45%
Customization
Change the stock symbol in the code:
pythonanalyze_stock("TSLA")  # Tesla
analyze_stock("GOOGL") # Google
analyze_stock("MSFT")  # Microsoft

5. **Commit message:** `Add README for stock analyzer project`
6. **Click "Commit new file"**

### Step 2: Add Requirements File
1. **Click "Add file"** again
2. **Create new file**
3. **Filename:** `requirements.txt`
4. **Content:**
yfinance==0.2.18
pandas==2.0.3
5. **Commit message:** `Add requirements file`
6. **Click "Commit new file"**

After these steps, your project folder will be complete with:
- ✅ `stock_analyzer.py` (your code)
- ✅ `README.md` (documentation) 
- ✅ `requirements.txt` (dependencies)

Try adding the README first and let me know how it goes!
