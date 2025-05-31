def test_sentiment_range():
    assert df['sentiment_score'].between(-1, 1).all()
