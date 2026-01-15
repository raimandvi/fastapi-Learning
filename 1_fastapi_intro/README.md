# FastAPI Introduction

This repository contains my first FastAPI application created as part of my FastAPI learning journey.

## 📌 What I learned
- What FastAPI is
  FastAPI - FastAPI is a Python framework which is used for creating Backend APIs.
            Used for giving data to Frontend and Mobile app.
- How to create a FastAPI app
- How to create a basic GET API
- How to run FastAPI using Uvicorn
- How to use Swagger UI for API testing

## 🚀 Technologies Used
- Python
- FastAPI
- Uvicorn

## Code explanation
- from fastapi import FastAPI (#importing fastapi class)

- app = FastAPI()  (#creating object of FastAPI class)

- @app.get("/")  (#it is a GET API endpoint)

- def root():
    return{"message": "Hello FastAPI"} (#response of API(JSON))

## ▶️ How to Run the Application

1. Install dependencies:
   ```bash
   pip install fastapi uvicorn
2. Run the server
   ```bash
   uvicorn main:app --reload
3. Open in browser:

   . API: http://127.0.0.1:8000/
   . Docs: http://127.0.0.1:8000/docs




