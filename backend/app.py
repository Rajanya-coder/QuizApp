from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

DATA_DIR = os.path.dirname(__file__)

@app.route("/questions/<topic>", methods=["GET"])
def get_questions(topic):
    with open(os.path.join(DATA_DIR, "questions.json")) as f:
        data = json.load(f)
    return jsonify(data.get(topic, [])[:5])

@app.route("/leaderboard", methods=["GET"])
def get_leaderboard():
    with open(os.path.join(DATA_DIR, "leaderboard.json")) as f:
        return jsonify(json.load(f))

@app.route("/leaderboard", methods=["POST"])
def post_leaderboard():
    new_score = request.json
    with open(os.path.join(DATA_DIR, "leaderboard.json"), "r+") as f:
        data = json.load(f)
        # Check if the exact entry already exists to prevent duplicates
        if new_score not in data:
            data.append(new_score)
            f.seek(0)
            f.truncate()  # Clear the file before writing new content
            json.dump(data, f, indent=4)
    return jsonify({"status": "success"})

if __name__ == "__main__":
    app.run(debug=True)

