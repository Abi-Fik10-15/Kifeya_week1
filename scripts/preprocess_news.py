# scripts/preprocess_news.py

import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')
sid = SentimentIntensityAnalyzer()

def preprocess_news_df(df):
    df = df.copy()
    df['sentiment'] = df['headline'].apply(lambda x: sid.polarity_scores(str(x))['compound'])
    df['published'] = pd.to_datetime(df['published'])
    df = df[['published', 'sentiment']]
    return df
