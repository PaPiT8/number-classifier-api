from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS

# Function to check if a number is prime
def is_prime(n):
    if n < 2 or not float(n).is_integer():  # Prime is for positive integers only
        return False
    n = int(n)
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Function to check if a number is an Armstrong number
def is_armstrong(n):
    if n < 0 or not float(n).is_integer():  # Only non-negative integers
        return False
    num_str = str(int(n))
    power = len(num_str)
    return int(n) == sum(int(digit) ** power for digit in num_str)

# Function to check if a number is perfect
def is_perfect(n):
    if n <= 0 or not float(n).is_integer():  # Positive integers only
        return False
    n = int(n)
    return n == sum(i for i in range(1, n) if n % i == 0)

# Function to get a fun fact from Numbers API
def get_fun_fact(number):
    try:
        response = requests.get(f'http://numbersapi.com/{number}/math?json')
        if response.status_code == 200:
            return response.json().get('text')
    except:
        return "No fun fact available."

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    number = request.args.get('number')

    # ✅ Input validation
    try:
        # Try to convert to float or int, don't raise error for negative or float values
        number = float(number) if '.' in number else int(number)
    except (ValueError, TypeError):
        return jsonify({"number": number, "error": True}), 400

    # Ensure the number is valid and handle negative/floating point numbers correctly
    if number is None:
        return jsonify({"number": number, "error": True}), 400

    properties = []
    if is_armstrong(number):
        properties.append("armstrong")
    properties.append("even" if int(number) % 2 == 0 else "odd")

    result = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": sum(int(d) for d in str(abs(int(number)))) if float(number).is_integer() else None,
        "fun_fact": get_fun_fact(number)
    }

    return jsonify(result), 200  # Always return 200 for valid numbers

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)  # Make the API publicly accessible
