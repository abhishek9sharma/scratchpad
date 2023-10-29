import ray
import requests
from fastapi import FastAPI
from ray import serve

app = FastAPI()


@serve.deployment
@serve.ingress(app)
class MyFastAPIDeployment:
    @app.get("/")
    def root(self):
        return "Hello, world!"


serve.run(MyFastAPIDeployment.bind(), route_prefix="/hello",port=8000, host="0.0.0.0")