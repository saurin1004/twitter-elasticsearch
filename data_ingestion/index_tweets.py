import os

from dotenv import load_dotenv
from elasticsearch import Elasticsearch
import pandas as pd

# Elasticsearch connection (credentials come from .env, see .env.example)
load_dotenv()
es = Elasticsearch(
    os.getenv("ELASTIC_HOST", "https://localhost:9200"),
    basic_auth=(os.getenv("ELASTIC_USER", "elastic"), os.getenv("ELASTIC_PASSWORD")),
    verify_certs=False,  # local development cluster with a self-signed certificate
)

# Load tweets
tweets_df = pd.read_csv("tweets.csv")

# Index tweets
for _, row in tweets_df.iterrows():
    es.index(index="tweets", id=row["tweet_id"], body={
        "timestamp": row["timestamp"],
        "text": row["text"]
    })

print("Tweets indexed in Elasticsearch.")
