from elasticsearch import Elasticsearch

# Elasticsearch connection details
es = Elasticsearch(
    "https://localhost:9200",  # Elasticsearch endpoint
    basic_auth=("elastic", "m-tQ7VooPxgmyjErjLwG"),  # Replace 'your_password' with the actual password
    verify_certs=False  # Set to False to skip SSL verification (not recommended for production)
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
