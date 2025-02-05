from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse, FileResponse
import requests

app = FastAPI(title="Number Classification API")

"""Enable CORS for all origins"""
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

"""Mount static directory for serving static files like favicon.ico."""
app.mount("/static", StaticFiles(directory="static"), name="static")

"""Root endpoint with a welcome message"""
@app.get("/")
async def read_root():
    return {
        "message": "Welcome to the Number Classification API! Use /api/classify-number?number=<number> to classify a number."
    }

"""Favicon endpoint to serve the favicon.ico file."""
@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("static/favicon.ico")

def is_armstrong(n: int) -> bool:
    """Check if a number is an Armstrong number."""
    digits = [int(d) for d in str(abs(n))]  # Ensure works for negative numbers
    return abs(n) == sum(d**len(digits) for d in digits)

def is_prime(n: int) -> bool:
    """Check if a number is a prime number."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n: int) -> bool:
    """Check if a number is a perfect number."""
    if n < 2:
        return False
    divisors = [i for i in range(1, abs(n)) if n % i == 0]
    return sum(divisors) == abs(n)  # Fix: Compare sum(divisors) to abs(n)

def get_fun_fact(n: float) -> str:
    """Get a fun fact from Numbers API."""
    response = requests.get(f"http://numbersapi.com/{int(n)}/math?json")  # Convert float to int
    if response.status_code == 200:
        data = response.json()
        return data.get("text", "No fun fact available.")  # Ensure string response
    return "No fun fact available."

def validate_number(number: str) -> float:
    """Validate and convert the input number to an integer or float."""
    try:
        num = float(number)  # Accepts integers and floating-point numbers
        return num
    except ValueError:
        return None  # Return None for invalid input

@app.get("/api/classify-number")
async def classify_number(number: str = Query(..., description="The number to classify")):
    num = validate_number(number)

    # ✅ Return a valid JSON error response if input is invalid
    if num is None:
        return JSONResponse(
            status_code=400,
            content={"number": number, "error": True},
            headers={"Content-Type": "application/json"}
        )

    properties = ["armstrong"] if is_armstrong(int(num)) else []
    properties.append("even" if int(num) % 2 == 0 else "odd")

    return JSONResponse(
        status_code=200,
        content={
            "number": num,  # ✅ Supports floats, negatives
            "is_prime": is_prime(int(num)),
            "is_perfect": is_perfect(int(num)),
            "properties": properties,
            "digit_sum": sum(int(digit) for digit in str(abs(int(num)))), 
            "fun_fact": get_fun_fact(num)  # ✅ Ensures fun_fact is always a string
        },
        headers={"Content-Type": "application/json"}
    )
