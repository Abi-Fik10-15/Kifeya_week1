import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')

def apply_vader_sentiment(news_df, text_col='headline'):
    sid = SentimentIntensityAnalyzer()
    news_df['sentiment'] = news_df[text_col].apply(lambda x: sid.polarity_scores(str(x))['compound'])
    return news_df
