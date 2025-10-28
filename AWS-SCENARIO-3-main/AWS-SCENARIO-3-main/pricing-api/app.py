# ~/dynamicpricing/pricing-api/app.py
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to Pricing API"})

@app.route('/calculate_price', methods=['POST'])
def calculate_price():
    data = request.json
    base_price = data.get('base_price', 100)
    demand_factor = data.get('demand_factor', 1.0)
    final_price = base_price * demand_factor
    return jsonify({"final_price": final_price})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

