# app/main.py
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from numutils import (
    is_prime, 
    is_armstrong_number, 
    get_digit_sum, 
    get_fun_fact
)
import math

app = FastAPI()

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/classify-number", response_class=JSONResponse)
async def classify_number(number: str = Query(..., min_length=1)):
    try:
        # Convert input to float first
        n = float(number)

        # Convert to integer if it is a whole number
        if n.is_integer():
            n = int(n)

        # Determine properties
        properties = []
        if isinstance(n, int):  # Only integers should be classified as even/odd or Armstrong
            properties.append("even" if n % 2 == 0 else "odd")

            # Only non-negative integers can be Armstrong numbers
            if n >= 0 and is_armstrong_number(n):
                properties.append("armstrong")

        # Construct response
        return JSONResponse(
            status_code=200,
            content={
                "number": n,
                "is_prime": is_prime(n) if isinstance(n, int) and n > 1 else False,  # Only check for primes if n > 1
                "is_perfect": False,  # Placeholder (you can add perfect number logic)
                "properties": properties,
                "digit_sum": get_digit_sum(abs(int(n))) if isinstance(n, int) else sum(int(d) for d in str(abs(n)) if d.isdigit()),
                "fun_fact": get_fun_fact(abs(int(n))) if isinstance(n, int) else "No specific fun fact for non-integer numbers"
            }
        )

    except ValueError:
        # Handle invalid input (non-numeric values)
        return JSONResponse(
            status_code=400,
            content={
                "number": number,
                "error": True,
                "message": "Invalid number format"
            }
        )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)