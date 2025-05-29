# scripts/features_sentiment.py

import pandas as pd

def merge_news_with_stock_data(news_df, stock_df):
    stock_df = stock_df.copy()
    news_df = news_df.copy()

    news_df['published'] = pd.to_datetime(news_df['published']).dt.date
    stock_df['Date'] = pd.to_datetime(stock_df.index).date

    daily_sentiment = news_df.groupby('published')['sentiment'].mean().reset_index()
    merged = pd.merge(stock_df.reset_index(), daily_sentiment, left_on='Date', right_on='published', how='left')

    # Fill missing sentiment with 0
    merged['sentiment'].fillna(0, inplace=True)

    # Target: next day price movement
    merged['target'] = (merged['Close'].shift(-1) > merged['Close']).astype(int)

    features = merged[['Open', 'High', 'Low', 'Close', 'Volume', 'sentiment']].dropna()
    features['target'] = merged['target']
    return features.dropna()
