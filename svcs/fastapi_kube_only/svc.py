import os
import sys
import time
import requests
from fastapi import APIRouter, FastAPI


app = FastAPI()


@app.post("/predict")
def predict(pred_req):
    pred_req["response"] = "responded from server"
    return pred_req


@app.get("/internal/healthcheck")
def healthcheck():
    return {"status": "200"}


@app.get("/")
def start_svc():
    return {"Info": "Prediction Service is running"}


