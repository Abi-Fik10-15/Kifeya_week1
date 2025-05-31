from pynance import data

# Retrieve data for MSFT
msft = data.get('MSFT', '2023-01-01', '2023-12-31')

# Calculate rolling volatility (standard deviation of daily returns)
msft['returns'] = msft['close'].pct_change()
msft['volatility'] = msft['returns'].rolling(window=20).std()

# Plot volatility
msft[['close', 'volatility']].plot(subplots=True, figsize=(12, 6), title="MSFT Price and Volatility")
