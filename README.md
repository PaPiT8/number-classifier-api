# number-classifier-api

## table of contents
- [overview](#overview)
- [technology stack](#technology-stack)
- [project structure](#project-structure)
- [installation](#installation)
- [local development](#local-development)
- [API endpoints](#api-endpoints)
- [deploy to AWS](deploy-to-AWS)
  
## overview
- **number classification:**
  - evaluates if the number is an armstrong number.
  - checks if the number is prime.
  - checks if the number is a perfect number.
  - calculate the sum of the digits.
  - indicates if the number is odd or even.
    
- **fun fact integration:**
  - obtains a fascinating mathematical fact from the numbers API.
    
- **CORS enabled:**
  - allows cross-origin requests.
    
- **static file handling:**
  - serves a favicon from the static directory.
    
- **deployment ready:**
  - configured to run as a serverless function.

## technology stack
- **python 3.8+**
- **fastAPI:** for building the API.
- **uvicorn** ASGI server for running the fastAPI app.
- **requests:** for HHTP requests to the numbers API.
- **aws EC2 instance:** deployment

## project structure 
- **main.py:** includes all the API logic, endpoints, and helper functions...
- **static/favicon.ico:** a favicon file to serve for the endpoint `/favicon.ico`.
- **requirements.txt:** compile a list of required packages and their versions.

## installation
**clone the repository:**
```bash
git clone https://github.com/PaPiT8/number-classifier-api.git
```
**create and activate a virtual environment:**
```
python -m venv venv
```
```
on macOS/linux:
source venv/bin/activate
```
```
on windows:
venv\Scripts\activate
```
**install dependencies:**
```
pip install -r requirements.txt
```

## local development
ensure you have the static directory and favicon.ico file in it.

run the application using uvicorn:
```
uvicorn main:app --reload
```
## API endpoints:

root endpoint: http://127.0.0.1:8000/  

API endpoint: http://127.0.0.1:8000/api/classify-number?number=371  

swagger UI documentation: http://127.0.0.1:8000/docs

## deploy to AWS
<<<<<<< HEAD
https://dev.to/papit8/configuring-nginx-web-server-on-amazon-ec2-my-experience-45nf



  
=======
https://dev.to/papit8/configuring-nginx-web-server-on-amazon-ec2-my-experience-45nf
>>>>>>> updated main.py
