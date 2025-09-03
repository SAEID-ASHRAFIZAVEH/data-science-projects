import yfinance as yf
import pandas as pd

def analyze_stock(symbol):
    # Download stock data for the last 30 days
    stock = yf.download(symbol, period="30d")
    
    # Calculate key metrics
    current_price = float(stock['Close'].iloc[-1])
    highest_price = float(stock['High'].max())
    lowest_price = float(stock['Low'].min())
    avg_price = float(stock['Close'].mean())
    price_change = float(((current_price - stock['Close'].iloc[0]) / stock['Close'].iloc[0]) * 100)
    
    # Display results
    print(f"\n📈 Stock Analysis for {symbol.upper()}")
    print(f"Current Price: ${current_price:.2f}")
    print(f"30-Day High: ${highest_price:.2f}")
    print(f"30-Day Low: ${lowest_price:.2f}")
    print(f"Average Price: ${avg_price:.2f}")
    print(f"30-Day Change: {price_change:.2f}%")

# Example usage
analyze_stock("AAPL")
