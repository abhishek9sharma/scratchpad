import os
import sys

import torch
from ray import serve
from starlette.requests import Request

# load model
root_folder = "/scratchpad"
sys.path.append(root_folder)
print(sys.path)
from src.hfmodels.utils import (CodeGenForCausalLM, generate_tokens,
                                get_device, load_artefacts)

# root_folder = os.path.join( "..","..",os.getcwd())
# print(root_folder)
# model_path = "/scratchpad/data/models/codegen-350M-mono"
# loaded_model, loaded_tokenizer, device =


# 1: Define a Ray Serve deployment.
@serve.deployment  # (num_replicas=1, ray_actor_options={"num_cpus": 4,"num_gpus": 1})
class LLMServe:
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

    async def __call__(self, request: Request) -> str:
        input = await request.json()
        # return str(self.device)
        resp = self._get_prediction(input["prompt"])
        resp["device"] = str(self.device)
        return resp
