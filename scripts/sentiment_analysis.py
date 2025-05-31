from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
import nltk
nltk.download('vader_lexicon')

def add_vader_sentiment(df, text_col='headline'):
    sid = SentimentIntensityAnalyzer()
    df['sentiment'] = df[text_col].apply(lambda x: sid.polarity_scores(str(x))['compound'])
    return df

def compute_daily_sentiment(news_df, date_col='date'):
    daily_sentiment = news_df.groupby(date_col)['sentiment'].mean().reset_index()
    daily_sentiment.rename(columns={'sentiment': 'avg_daily_sentiment'}, inplace=True)
    return daily_sentiment

