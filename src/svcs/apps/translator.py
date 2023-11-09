import ray
from fastapi import FastAPI
from ray import serve
from starlette.requests import Request
from transformers import pipeline

app = FastAPI()


@serve.deployment(num_replicas=1, ray_actor_options={"num_cpus": 0.2, "num_gpus": 0})
@serve.ingress(app)
class Translator:
    def __init__(self):
        # Load model
        self.model = pipeline("translation_en_to_fr", model="t5-small")

    @app.post("/")
    async def translate(self, request: Request) -> str:
        # Run inference
        data = await request.json()
        model_output = self.model(data["prompt"])

        # Post-process output to return only the translation text
        translation = model_output[0]["translation_text"]

        return translation


# translator_app = Translator.bind()
