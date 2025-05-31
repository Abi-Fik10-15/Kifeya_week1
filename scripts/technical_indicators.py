import pandas as pd
import yfinance as yf
import talib
import matplotlib.pyplot as plt

# Download data using yfinance
df = yf.download("AAPL", start="2023-01-01", end="2023-12-31")

# Calculate Technical Indicators using TA-Lib
df['SMA_20'] = talib.SMA(df['Close'], timeperiod=20)
df['RSI'] = talib.RSI(df['Close'], timeperiod=14)
macd, macdsignal, macdhist = talib.MACD(df['Close'])
df['MACD'] = macd
df['MACD_Signal'] = macdsignal

# Visualize moving average
plt.figure(figsize=(12, 6))
plt.plot(df['Close'], label='Close Price')
plt.plot(df['SMA_20'], label='SMA 20')
plt.title('Apple Stock with 20-Day SMA')
plt.legend()
plt.show()
