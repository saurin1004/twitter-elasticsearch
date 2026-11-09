# Twitter × Elasticsearch: Tweet Search and Sentiment Analysis

An end-to-end pipeline that collects tweets from the Twitter (X) API v2, scores their sentiment, indexes them in **Elasticsearch** for full-text search and serves search results and interactive charts through a **Flask** app.

## Pipeline

```
Twitter API v2 ──► fetch_tweets.py ──► tweets.csv
                                         │
                       add_sentiment_score.py (TextBlob polarity)
                                         │
                                         ▼
                              tweets_with_sentiment.csv
                                         │
                index_tweets.py ──► Elasticsearch index "tweets"
                                         │
                                Flask app (app.py)
                     /search?q=… · sentiment chart · top-words chart
```

| Step | Script | What it does |
| --- | --- | --- |
| Collect | `data_collection/fetch_tweets.py` | Pulls recent tweets for a keyword via `tweepy.Client` (API v2) and saves them to `tweets.csv` |
| Enrich | `sentiment_analysis/add_sentiment_score.py` | Adds a TextBlob sentiment polarity score (-1 to 1) to each tweet |
| Index | `data_ingestion/index_tweets.py` | Indexes the tweets into Elasticsearch (`tweets` index) |
| Report | `reporting/interactive_charts.py` | Builds Plotly charts: sentiment distribution and the top 10 words (stop words removed) |
| Serve | `app.py` | Flask app with full-text search over tweet text and the chart pages |
| Query | `sentiment_analysis/Backend-Api.py` | Example query against the index |

## Tech stack

Python · Elasticsearch 8 · Kibana · Flask · Tweepy (Twitter API v2) · TextBlob · NLTK · pandas · Plotly

## Running locally

Requirements: Python 3.10+, a local Elasticsearch 8 instance (Kibana optional) and a Twitter developer account.

```bash
git clone https://github.com/saurin1004/twitter-elasticsearch.git
cd twitter-elasticsearch

python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

cp .env.example .env    # add your Twitter and Elasticsearch credentials
```

Start Elasticsearch, for example `bin/elasticsearch` from your install directory. It listens on `https://localhost:9200`. Then run the pipeline:

```bash
python data_collection/fetch_tweets.py               # writes tweets.csv (keyword set in the script)
python sentiment_analysis/add_sentiment_score.py     # writes tweets_with_sentiment.csv
python data_ingestion/index_tweets.py                # indexes into Elasticsearch
python reporting/interactive_charts.py               # writes the chart HTML files
cp sentiment_distribution.html top_words.html templates/
flask --app app run                                  # http://127.0.0.1:5000
```

### Endpoints

| Route | Description |
| --- | --- |
| `GET /` | Home page |
| `GET /search?q=<text>` | Full-text (`multi_match`) search over tweet text and returns matching documents |
| `GET /Sentiment distribution` | Interactive sentiment histogram |
| `GET /Top words` | Top 10 words bar chart |

Sample data (`tweets.csv`, `tweets_with_sentiment.csv`) is included, so you can skip the collection step and start from indexing.

## Acknowledgments

- [Elasticsearch](https://www.elastic.co/elasticsearch): search and analytics engine
- [Twitter / X API](https://developer.x.com/en/docs/x-api): tweet data
