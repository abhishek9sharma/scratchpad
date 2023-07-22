import os
import sys
import time

import requests
from fastapi import APIRouter, FastAPI

app = FastAPI()


@app.post("/serve")
def serve(req):
    return req + " responded from server"


@app.get("/internal/healthcheck")
def healthcheck():
    return {"status": "200"}


@app.get("/")
def start_svc():
    return {"Info": "Service is running"}
