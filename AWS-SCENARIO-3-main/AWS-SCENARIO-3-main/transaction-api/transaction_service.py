# ~/dynamicpricing/transaction-api/transaction_service.py
from flask import Flask, jsonify, request
import random

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to Transaction API"})

@app.route('/process_transaction', methods=['POST'])
def process_transaction():
    data = request.json
    amount = data.get('amount', 0)
    transaction_id = random.randint(1000, 9999)
    status = "Success" if amount < 10000 else "Pending Review"
    return jsonify({"transaction_id": transaction_id, "status": status})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
