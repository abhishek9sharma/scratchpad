import argparse
import os
import sys
import time

import ray
# from ray_deployments.fast_api_ray import LLMServeFastAPI
# from svcs.apps.asyncsvc import ServeBatch
from apps.asyncsvc import ServeBatch
from ray import serve

#
# from ray_deployments.ray_only_svc import LLMServe
# from ray_deployments.ray_streaming_svc import StreamingResponder
# from ray_deployments.tgi_ray import TextGenerationInferenceDeployment
# from ray_deployments.translator import Translator
# from ray_deployments.hello_world import MyModelDeployment

if __name__ == "__main__":
    try:
        # parser = argparse.ArgumentParser()
        # parser.add_argument("deployment", help="Name of the deployment")
        # args = parser.parse_args()
        # deployment = args.deployment
        # print(f"Running {deployment}")

        # ray.init(dashboard_host="0.0.0.0", num_gpus=0)
        # time.sleep(100)

        # if deployment == "LLMServe":
        #    serve.run(LLMServe.bind(), host="0.0.0.0")
        # if deployment == "Translator":
        #    serve.run(Translator.bind(), host="0.0.0.0")
        # if deployment == "LLMServeFastAPI":
        serve.run(
            ServeBatch.options(
                num_replicas=1, ray_actor_options={"num_cpus": 1}
            ).bind(),
            route_prefix="/batch",
            port=8000,
            host="0.0.0.0",
        )
        # serve.deploy()
        # serve.run(MyModelDeployment.bind(), host="0.0.0.0")
        # if deployment == "TGI":
        # serve.run(
        #     TextGenerationInferenceDeployment.options(
        #         ray_actor_options={"num_gpus": 1}
        #     ).bind(model_id="/scratchpad/data/models/codegen-350M-mono", num_shard=1),
        #     host="0.0.0.0",
        # )
        # if deployment == "Streaming":
        #     serve.run(StreamingResponder.bind(), host="0.0.0.0")

        while True:
            time.sleep(10)
            print(serve.serve.status())
    except Exception as e:
        print(e)
    finally:
        pass
        # ray.shutdown()
