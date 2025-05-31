import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def merge_sentiment_with_prices(price_df, sentiment_df):
    price_df['date'] = pd.to_datetime(price_df['Date']).dt.date
    sentiment_df['date'] = pd.to_datetime(sentiment_df['date']).dt.date
    merged = pd.merge(price_df, sentiment_df, on='date', how='inner')
    merged['daily_return'] = merged['Close'].pct_change()
    return merged

def plot_correlation(df):
    sns.scatterplot(x='avg_daily_sentiment', y='daily_return', data=df)
    plt.title('Sentiment vs. Daily Stock Return')
    plt.xlabel('Average Daily Sentiment')
    plt.ylabel('Daily Return')
    plt.grid(True)
    plt.show()

    corr = df[['avg_daily_sentiment', 'daily_return']].corr()
    print("Correlation Matrix:\n", corr)
