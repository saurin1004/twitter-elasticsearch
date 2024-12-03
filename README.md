# Twitter Elasticsearch Integration

This project demonstrates how to integrate Twitter data with Elasticsearch for efficient searching, filtering, and analysis. It allows you to collect tweets, index them in Elasticsearch, and query the data with advanced search capabilities. This repository provides the code to set up the pipeline, from fetching data from the Twitter API to storing and querying it in Elasticsearch.

## Features

- Collects tweets from Twitter using the Twitter API.
- Indexes tweets in Elasticsearch for fast search and analytics.
- Allows querying of tweets by keywords, date ranges, hashtags, and more.
- Simple setup and configuration to get started with Elasticsearch and Twitter API integration.

## Requirements

- Python 3.x
- Elasticsearch (Docker or local installation)
- Twitter Developer Account (for API access)
- `pip` (Python package installer)

## Installation

### 1. Clone the Repository
Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/saurin1004/twitter-elasticsearch.git
cd twitter-elasticsearch
```

### 2. Install Dependencies
Install the required Python libraries using pip:

```bash
pip install -r requirements.txt
```

### 3. Set Up Twitter API Access
To fetch tweets, you'll need access to the Twitter API. Follow these steps to get your Twitter API keys:

Go to the Twitter Developer Portal.
Create an application and generate your API keys (API Key, API Secret Key, Access Token, Access Token Secret).
Once you have your credentials, create a .env file in the root directory and add the following environment variables:

```bash
TWITTER_API_KEY=your_api_key
TWITTER_API_SECRET_KEY=your_api_secret_key
TWITTER_ACCESS_TOKEN=your_access_token
TWITTER_ACCESS_TOKEN_SECRET=your_access_token_secret
```

### 4. Set Up Elasticsearch
You can either install Elasticsearch locally or use Docker to run it. 
I personally chose to install it locally. And then later went to folder and entered the following command in terminal:

```bash
bin/elasticsearch
```
Ensure that Elasticsearch is running on http://localhost:9200.

### 5. Set Up Kibana
You can either install Kibana locally or use Docker to run it. 
I personally chose to install it locally. And then later went to folder and entered the following command in terminal:

```bash
bin/kibana
```

## Usage

### 1. Fetch Tweets
To start fetching tweets from Twitter, run the fetch_tweets.py script. You can specify parameters such as search query, number of tweets, and language.

```bash
python data_collection/fetch_tweets.py --query "Python" --count 100 --language en
```

### 2. Index Tweets in Elasticsearch
After fetching tweets, you can index them in Elasticsearch using the index_tweets.py script. Make sure Elasticsearch is running before indexing.

```bash
python data_ingestion/index_tweets.py
```

### 3. Generate report
After indexing queries, we want to generate static webpages using plotly library.
```bash
python reporting/interactive_charts.py
```
Add these files to templates folder.

### 4. Search for Tweets
To query the indexed tweets, you can use the search_tweets.py script. Specify your search query and any filters.

```bash
flask --app app run
```

## Contributing

Feel free to open issues and create pull requests. If you have any ideas for improvement or feature suggestions, please share them.

## Acknowledgments

[Elasticsearch](https://www.elastic.co/elasticsearch) - Search and analytics engine.


[Twitter API](https://developer.x.com/en/docs/x-api) - Used for fetching tweets.
