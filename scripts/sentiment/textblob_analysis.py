from textblob import TextBlob

def apply_textblob_sentiment(df, col='headline'):
    df['textblob_score'] = df[col].apply(lambda x: TextBlob(str(x)).sentiment.polarity)
    return df
