from flask import Flask, jsonify
from main import get_latest_prices

app = Flask(__name__)

@app.route("/")
def home():
    return "PC Price Tracker is running"

@app.route("/prices")
def prices():
    # Returns latest scraped prices as JSON
    latest_prices = get_latest_prices()
    return jsonify(latest_prices)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
