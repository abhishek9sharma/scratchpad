import os
import sys

from ray import serve
from starlette.requests import Request

# load model
root_folder = os.path.join(os.getcwd(), "..")
sys.path.append(root_folder)
from src.hfmodels.utils import *

model_path = "/scratchpad/data/models/codegen-350M-mono"
loaded_model, loaded_tokenizer, device = load_artefacts(
    model_path, model_class=CodeGenForCausalLM
)


# 1: Define a Ray Serve deployment.
@serve.deployment
class LLMServe:
    def __init__(self) -> None:
        # All the initialization code goes here
        pass

    # def _run_prediction(self, text: str):
    #    gen = generate_tokens(loaded_model, loaded_tokenizer, device, text)
    #    return gen

    async def __call__(self, request: Request) -> str:
        return "HELLO"
        # # 1. Parse the request
        # text = request.query_params["text"]
        # # 2. Get Prediction
        # resp = self._get_prediction(text)
        # # 3. Return the response
        # return resp["text"]


# # 2: Bind the model to deployment
# deployment = LLMServe.bind()

# # 3: Run the deployment
# serve.api.run(deployment)
