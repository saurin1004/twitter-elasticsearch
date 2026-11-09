import os

from dotenv import load_dotenv
from elasticsearch import Elasticsearch

# Elasticsearch connection (credentials come from .env, see .env.example)
load_dotenv()
es = Elasticsearch(
    os.getenv("ELASTIC_HOST", "https://localhost:9200"),
    basic_auth=(os.getenv("ELASTIC_USER", "elastic"), os.getenv("ELASTIC_PASSWORD")),
    verify_certs=False,  # local development cluster with a self-signed certificate
)

# Define the query (Modify based on your use case)
query = {
    "query": {
        "match_all": {}  # Fetch all records; replace with a specific query if needed
    }
}

# Specify the index name
index_name = "tweets"  # Replace 'tweets' with your index name

try:
    # Execute the search query
    response = es.search(index=index_name, body=query)

    # Check if hits exist and print the results
    if response["hits"]["hits"]:
        print("Documents Found:")
        for doc in response["hits"]["hits"]:
            print(f"ID: {doc['_id']}, Source: {doc['_source']}")
    else:
        print("No documents found.")
except Exception as e:
    print(f"Error: {e}")
