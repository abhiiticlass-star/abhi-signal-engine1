from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "ABHI'S SIGNALS BACKEND RUNNING"

@app.route("/get-signal/<pair>")
def get_signal(pair):
    return jsonify({
        "pair": pair,
        "signal": "AVOID",
        "score": 50,
        "trend": "Neutral",
        "trendM5": "Neutral",
        "market": "open"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
