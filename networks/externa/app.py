from flask import Flask, request, json, jsonify
from requests import get

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET"])
def index():
    data = get("https://randomuser.me/api")
    return data.json()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
