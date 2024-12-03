# import plotly.express as px
# import pandas as pd

# # Load data
# tweets_df = pd.read_csv("tweets_with_sentiment.csv")

# # Sentiment distribution chart
# fig = px.histogram(tweets_df, x="sentiment", nbins=20, title="Sentiment Distribution")
# fig.write_html("sentiment_distribution.html")

# # Most common words (basic word cloud)
# tweets_df["text"] = tweets_df["text"].str.lower()
# word_counts = tweets_df["text"].str.split(expand=True).stack().value_counts().reset_index()
# word_counts.columns = ["word", "count"]
# fig = px.bar(word_counts.head(10), x="word", y="count", title="Top 10 Words")
# fig.write_html("top_words.html")

# print("Visualizations saved as HTML files.")
import plotly.express as px
import pandas as pd
from collections import Counter
import re

# Load data
tweets_df = pd.read_csv("tweets_with_sentiment.csv")

# Sentiment distribution chart
fig = px.histogram(tweets_df, x="sentiment", nbins=20, title="Sentiment Distribution")
fig.write_html("sentiment_distribution.html")

# Define a list of stop words (including filler words and common English words)
stop_words = set([
    "a", "an", "and", "are", "as", "at", "be", "by", "for", "from", "has", "he", 
    "in", "is", "it", "its", "of", "on", "that", "the", "to", "was", "were", "will", "with",
    "um", "uh", "oh", "er", "ah", "like", "just", "you know", "i mean", "i guess", 
    "totally", "literally", "seriously", "actually", "basically", "really", "very"
])

# Function to clean and tokenize text
def clean_and_tokenize(text):
    # Convert to lowercase and split into words
    words = text.lower().split()
    # Remove punctuation and filter out stop words
    words = [re.sub(r'[^\w\s]', '', word) for word in words if word not in stop_words]
    return [word for word in words if word]  # Remove empty strings

# Process tweets and count word frequencies
all_words = []
for tweet in tweets_df["text"]:
    all_words.extend(clean_and_tokenize(tweet))

# Count word frequencies
word_counts = Counter(all_words).most_common(10)

# Create a DataFrame for the top 10 words
top_words_df = pd.DataFrame(word_counts, columns=["word", "count"])

# Create bar chart for top 10 words
fig = px.bar(top_words_df, x="word", y="count", title="Top 10 Words (Excluding Stop Words)")
fig.write_html("top_words.html")

print("Visualizations saved as HTML files.")