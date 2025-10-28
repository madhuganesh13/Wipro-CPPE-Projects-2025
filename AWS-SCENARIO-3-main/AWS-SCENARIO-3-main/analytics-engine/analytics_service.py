# ~/dynamicpricing/analytics-engine/analytics_service.py
from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to Analytics Engine"})

@app.route('/summary')
def summary():
    total_transactions = random.randint(100, 1000)
    avg_price = round(random.uniform(50, 200), 2)
    return jsonify({
        "total_transactions": total_transactions,
        "average_price": avg_price
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
