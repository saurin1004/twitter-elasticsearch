from textblob import TextBlob
import pandas as pd

tweets_df = pd.read_csv("tweets.csv")

# Add sentiment analysis to tweets
def analyze_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

tweets_df["sentiment"] = tweets_df["text"].apply(analyze_sentiment)
tweets_df.to_csv("tweets_with_sentiment.csv", index=False)
print("Sentiment analysis completed and saved.")
