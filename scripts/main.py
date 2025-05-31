import pandas as pd
from src.data_loader import load_price_data, load_news_data
from src.sentiment_analysis import compute_sentiment, aggregate_daily_sentiment
from src.indicators import add_indicators
from src.correlation_analysis import correlation_plot, rolling_correlation

price_df = load_price_data('data/price_data.csv')
news_df = load_news_data('data/news_data.csv')

news_df = compute_sentiment(news_df)
daily_sentiment = aggregate_daily_sentiment(news_df)

price_df = add_indicators(price_df)
price_df['date'] = pd.to_datetime(price_df['date'])

merged = pd.merge(price_df, daily_sentiment, on='date', how='inner')
merged['daily_return'] = merged['Close'].pct_change()

correlation_plot(merged, ['Close', 'daily_return', 'RSI', 'MACD', 'sentiment_score'])
rolling_correlation(merged, 'daily_return', 'sentiment_score')
