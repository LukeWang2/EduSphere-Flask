from flask import Flask, request
import os, cockroach, keys, cohere, numpy as np

app = Flask(__name__)
co = cohere.Client(keys.cohere_key)


def calculate_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


@app.route("/api")
def debug():
    return "Hello world"


@app.route("/api/item-from-id")
def item_from_id():
    ids = request.args["id"]
    item = cockroach.get_item_by_id(ids)
    return {"name": item[1], "url": item[2]}


@app.route("/api/word-similarity")
def similarity():
    ans = request.args["ans"]
    guess = request.args["guess"]

    # get the embeddings
    (ans, guess) = co.embed(texts=[ans, guess]).embeddings

    return {"similarity": calculate_similarity(ans, guess)}


if __name__ == "__main__":
    app.run(port=os.getenv("PORT", 8000))
