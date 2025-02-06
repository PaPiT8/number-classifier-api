# app/number_utils.py
import math
import requests

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_armstrong_number(n):
    """Check if a number is an Armstrong number."""
    num_str = str(n)
    power = len(num_str)
    return sum(int(digit) ** power for digit in num_str) == n

def get_digit_sum(n):
    """Calculate the sum of digits."""
    return sum(int(digit) for digit in str(n))

def get_fun_fact(number):
    """Fetch a fun fact about the number from Numbers API."""
    try:
        response = requests.get(f"http://numbersapi.com/{number}/math")
        return response.text if response.status_code == 200 else "No fun fact available"
    except:
        return "No fun fact available"