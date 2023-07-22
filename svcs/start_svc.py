import argparse
import os
import sys
import time

import ray
from ray import serve
from ray_deployments.fast_api_ray import FastAPIWrapper
from ray_deployments.ray_only_svc import LLMServe
from ray_deployments.ray_streaming_svc import StreamingResponder
from ray_deployments.tgi_ray import TextGenerationInferenceDeployment
from ray_deployments.translator import Translator

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("deployment", help="Name of the deployment")
    args = parser.parse_args()
    deployment = args.deployment
    print(f"Running {deployment}")
    ray.init(dashboard_host="0.0.0.0")

    if deployment == "LLMServe":
        serve.run(LLMServe.bind(), host="0.0.0.0")
    if deployment == "Translator":
        serve.run(Translator.bind(), host="0.0.0.0")
    if deployment == "FastAPI":
        serve.run(FastAPIWrapper.bind(), host="0.0.0.0")
    if deployment == "TGI":
        serve.run(
            TextGenerationInferenceDeployment.options(
                ray_actor_options={"num_gpus": 1}
            ).bind(model_id="/scratchpad/data/models/codegen-350M-mono", num_shard=1),
            host="0.0.0.0",
        )
    if deployment == "Streaming":
        serve.run(StreamingResponder.bind(), host="0.0.0.0")

    while True:
        time.sleep(5)
        print(serve.list_deployments())
