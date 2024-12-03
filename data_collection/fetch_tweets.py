from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv("TWITTER_API_KEY")
SECRET_KEY = os.getenv("TWITTER_SECRET_KEY")
BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
# ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
# ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

import tweepy
import pandas as pd

# Twitter API credentials
api_key = API_KEY
api_key_secret = SECRET_KEY
# access_token = ACCESS_TOKEN
# access_token_secret = ACCESS_TOKEN_SECRET

# # Authenticate with the Twitter API
# auth = tweepy.OAuthHandler(api_key, api_key_secret)
# auth.set_access_token(access_token, access_token_secret)
# api = tweepy.API(auth)

# # Function to fetch tweets
# def fetch_tweets(keyword, max_tweets=100):
#     tweets = tweepy.Cursor(api.search_tweets, q=keyword, lang="en", tweet_mode="extended").items(max_tweets)
#     data = [{"tweet_id": tweet.id_str, "timestamp": tweet.created_at, "text": tweet.full_text} for tweet in tweets]
#     return pd.DataFrame(data)

# # Fetch tweets
# tweets_df = fetch_tweets(keyword="AI", max_tweets=100)
# tweets_df.to_csv("tweets.csv", index=False)
# print("Tweets_saved_to_tweets.csv")

bearer_token = BEARER_TOKEN

# Authenticate with Twitter API v2
client = tweepy.Client(bearer_token=bearer_token)

# Function to fetch tweets
def fetch_tweets_v2(keyword, max_tweets=100):
    tweets = client.search_recent_tweets(
        query=keyword, 
        max_results=min(max_tweets, 100),  # Twitter API allows max 100 per request
        tweet_fields=["id", "created_at", "text"]
    )
    data = [{"tweet_id": tweet.id, "timestamp": tweet.created_at, "text": tweet.text} for tweet in tweets.data]
    return pd.DataFrame(data)

# Fetch tweets
try:
    tweets_df = fetch_tweets_v2(keyword="AI", max_tweets=100)
    tweets_df.to_csv("tweets.csv", index=False)
    print("Tweets saved to tweets.csv")
except Exception as e:
    print(f"Error: {e}")