from fastapi import FastAPI
from router import route_request

app = FastAPI()

@app.post("/route")
def route(payload: dict):
    return route_request(payload)