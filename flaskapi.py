from flask import Flask, request
import os, cockroach

app = Flask(__name__)


@app.route("/api")
def debug():
    return "Hello world"


@app.route("/api/item-from-id")
def item_from_id():
    ids = request.args["id"]
    item = cockroach.get_item_by_id(ids)
    return {"name": item[1], "url": item[2]}


if __name__ == "__main__":
    app.run(port=os.getenv("PORT", 8000))
