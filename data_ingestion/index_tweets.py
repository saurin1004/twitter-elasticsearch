from elasticsearch import Elasticsearch
# from dotenv import load_dotenv
# import os
import pandas as pd

# PASSWORD = os.getenv("ELASTIC_PASSWORD")

# Connect to Elasticsearch
es = Elasticsearch('https://localhost:9200', basic_auth=('elastic', 'm-tQ7VooPxgmyjErjLwG'), verify_certs=False)

# Load tweets
tweets_df = pd.read_csv("tweets.csv")

# Index tweets
for _, row in tweets_df.iterrows():
    es.index(index="tweets", id=row["tweet_id"], body={
        "timestamp": row["timestamp"],
        "text": row["text"]
    })

print("Tweets indexed in Elasticsearch.")
