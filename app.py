from flask import Flask, request, jsonify, render_template
from elasticsearch import Elasticsearch

app = Flask(__name__)

# Elasticsearch connection
es = Elasticsearch(
    "https://localhost:9200",
    basic_auth=("elastic", "m-tQ7VooPxgmyjErjLwG"),  # Use your credentials
    verify_certs=False,
)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/Sentiment distribution")
def page1():
    return render_template("sentiment_distribution.html")

@app.route("/Top words")
def page2():
    return render_template("top_words.html")

@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("q")
    if not query:
        return jsonify({"error": "Query parameter 'q' is required"}), 400

    try:
        res = es.search(
            index="tweets",
            body={"query": {"multi_match": {"query": query, "fields": ["text"]}}},
        )
        # print(res["hits"]["hits"])
        return jsonify(res["hits"]["hits"])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# @app.route("/search")
# def search():
#     query = request.args.get("q")
#     if not query:
#         return jsonify({"error": "Query parameter 'q' is required"}), 400

#     body = {
#         "query": {
#             "multi_match": {
#                 "query": query,
#                 "fields": ["text"],
#                 "fuzziness": "AUTO"
#             }
#         }
#     }

#     try:
#         res = es.search(index="tweets", body=body)
#         return jsonify(res["hits"]["hits"])
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)