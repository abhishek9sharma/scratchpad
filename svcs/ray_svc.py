import os
import sys
import time

import requests
from fastapi import APIRouter, FastAPI
from ray import serve

root_folder = os.path.join(os.getcwd(), "..")
sys.path.append(root_folder)
from src.hfmodels.utils import *

router = APIRouter()
model_path = "/scratchpad/data/models/codegen-350M-mono"
loaded_model, loaded_tokenizer, device = load_artefacts(
    model_path, model_class=CodeGenForCausalLM
)

# @router.post("/predict")
# app.include_router(prediction_router.router, tags=["make predictions"])

app = FastAPI()


@app.post("/predict")
def predict(pred_req):
    gen = generate_tokens(loaded_model, loaded_tokenizer, device, pred_req)
    return gen


@app.get("/internal/healthcheck")
def healthcheck():
    return {"status": "200"}


@app.get("/")
def start_svc():
    return {"Info": "Prediction Service is running"}


# @serve.deployment(
#     route_prefix="/predict",
#     num_replicas=1,
#     #ray_actor_options={"num_cpus": 1, "num_gpus": 0.5}
# )


@serve.deployment  # (num_replicas=1, ray_actor_options={"num_gpus": 1})
@serve.ingress(app)
class FastAPIWrapper:
    pass


# serve.run(FastAPIWrapper.bind(), host="0.0.0.0")

# while True:
#     time.sleep(5)
#     print(serve.list_deployments())
# # resp = requests.get("http://localhost:8000/")
