import sys
import time

import ray
import requests
from fastapi import FastAPI
from pydantic import BaseModel
from ray import serve
from starlette.requests import Request

from src.core.hfmodels.utils import (CodeGenForCausalLM, generate_tokens,
                                     get_device, load_artefacts)

# load model
root_folder = "/scratchpad"
sys.path.append(root_folder)
print(sys.path)


class PredReq(BaseModel):
    prompt: str


app = FastAPI()


# , ray_actor_options={"num_cpus": 1, "num_gpus": 1})
@serve.deployment(num_replicas=1)
@serve.ingress(app)
class LLMServeFastAPI:
    def __init__(self) -> None:
        # pass
        # All the initialization code goes here
        self.model_path = "/scratchpad/data/models/codegen-350M-mono"
        self.device = get_device()
        self.model, self.tokenizer, self.device = load_artefacts(
            self.model_path, model_class=CodeGenForCausalLM
        )

    def _get_prediction(self, text: str):
        gen = generate_tokens(self.model, self.tokenizer, self.device, text)
        return gen

    # async def __call__(self, request: Request) -> str:
    #     input = await request.json()
    #     # return str(self.device)
    #     resp = self._get_prediction(input["prompt"])
    #     resp["device"] = str(self.device)
    #     return resp

    @app.post("/predict")
    def predict(self, request: PredReq):
        # input =  request.json()
        # return str(self.device)
        resp = self._get_prediction(request.prompt)
        resp["device"] = str(self.device)
        return {"resp": resp}


# fastapp = MyFastAPIDeployment.bind()
serve.run(LLMServeFastAPI.bind(), route_prefix="/LLMFastAPI", port=8000, host="0.0.0.0")

while True:
    time.sleep(10)
    print(serve.status())
