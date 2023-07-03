import os
import time

import ray
from fastapi_svc import FastAPIWrapper
from ray import serve
from ray_svc import LLMServe

ray.init(dashboard_host="0.0.0.0")

serve.run(LLMServe.bind(), host="0.0.0.0")
# LMServe.deploy()
# serve.run(FastAPIWrapper.bind(), host="0.0.0.0")
# FastAPIWrapper.deploy()

while True:
    time.sleep(5)
    print(serve.list_deployments())
