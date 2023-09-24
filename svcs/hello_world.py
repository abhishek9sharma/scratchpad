import ray
ray.init(dashboard_host="0.0.0.0")
import requests
from starlette.requests import Request
from typing import Dict

from ray import serve


# 1: Define a Ray Serve application.
@serve.deployment
class MyModelDeployment:
    def __init__(self, msg: str):
        # Initialize model state: could be very large neural net weights.
        self._msg = msg

    def __call__(self, request: Request) -> Dict:
        return {"result": self._msg}


app = MyModelDeployment.bind(msg="Hello world!")
serve.run(app, host="0.0.0.0")
#print(requests.get("http://127.0.0.1:8000/").json())

import time
while True:
    time.sleep(5)
    print(serve.list_deployments())

# # # # 3: Query the application and print the result.

# # {'result': 'Hello world!'}