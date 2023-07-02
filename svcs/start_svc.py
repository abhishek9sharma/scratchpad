import time

import ray
from ray import serve
from fastapi_svc import FastAPIWrapper

ray.init(dashboard_host="0.0.0.0")
serve.run(FastAPIWrapper.bind(), host="0.0.0.0")
# serve.start(host="0.0.0.0")
FastAPIWrapper.deploy()

while True:
    time.sleep(5)
    print(serve.list_deployments())
