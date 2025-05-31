import pandas as pd
import yfinance as yf

# Load stock price data (e.g., Apple)
def load_stock_data(ticker='AAPL', start='2023-01-01', end='2023-12-31'):
    df = yf.download(ticker, start=start, end=end)
    df.to_csv('data/stock_data.csv')
    return df

# Load news dataset (CSV format expected)
def load_news_data(filepath='data/news_headlines.csv'):
    df = pd.read_csv(filepath)
    return df
