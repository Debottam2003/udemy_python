# from flask import Flask

# app = Flask(__name__)

# @app.get("/")
# def home():
#     return "hello world"

# @app.post("/")
# def save():
#     return "data saved"

# if __name__ == "__main__":
#     print("Hello from proj!")
#     app.run(host="127.0.0.1", port=3333, debug=True)

from fastapi import FastAPI
from uvicorn import run

app = FastAPI()

@app.get("/")
def home():
    return {"data": {"name": "debottam kar", "age": 22}}

run(app, host="127.0.0.1", port=3333)