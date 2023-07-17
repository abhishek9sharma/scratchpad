#ref : https://gist.github.com/Yard1/7dd3ae5f9002a7ed9b0b4f1f2dfe3375
#text-generation-launcher --model-id Salesforce/codegen-350M-multi --num-shard 1 --master-addr 0.0.0.0 --port 8080
import logging
import signal
import subprocess
import time
from typing import List, Optional

import psutil
import requests
from fastapi import FastAPI
from pydantic import BaseModel
from ray import serve
from ray.train._internal.utils import get_address_and_port
from starlette.responses import StreamingResponse
from text_generation import Client

app = FastAPI()
logger = logging.getLogger(__name__)


def generate_stream_text(client: Client, *args, **kwargs):
    for response in client.generate_stream(*args, **kwargs):
        if not response.token.special:
            yield response.token.text
            time.sleep(1)


class GenerateStream(BaseModel):
    prompt: str
    do_sample: bool = False
    max_new_tokens: int = 20
    repetition_penalty: Optional[float] = None
    return_full_text: bool = False
    seed: Optional[int] = None
    stop_sequences: Optional[List[str]] = None
    temperature: Optional[float] = None
    top_k: Optional[int] = None
    top_p: Optional[float] = None
    truncate: Optional[int] = None
    typical_p: Optional[float] = None
    watermark: bool = False


# def kill_orphans():
#     for proc in psutil.process_iter():
#         if (
#             "text-generation" in proc.name()
#             and "text-generation" not in proc.parent().name()
#             and "ray" not in proc.parent().name()
#         ):
#             proc.send_signal(signal.SIGTERM)


@serve.deployment
@serve.ingress(app)
class TextGenerationInferenceDeployment:
    def __init__(
        self,
        #model_id: str,
        #num_shard: int,
        #port: Optional[int] = None,
        #extra_args: List[str] = None,
    ) -> None:
        #kill_orphans()
        #self.model_id = model_id
        #self.ip, self.port = port or get_address_and_port()
        #self.torch_port = self.port
        self.ip = "127.0.0.1"
        self.port=8080
        # while self.torch_port == self.port:
        #     _, self.torch_port = get_address_and_port()

        # self.process = subprocess.Popen(
        #     [
        #         "text-generation-launcher",
        #         "--model-id",
        #         self.model_id,
        #         "--num-shard",
        #         str(num_shard),
        #         "--port",
        #         str(self.port),
        #         "--master-addr",
        #         self.ip,
        #         "--master-port",
        #         str(self.torch_port),
        #     ]
        #     + (extra_args or []),
        # )
        starting = True
        # time.sleep(10)
        client = Client(f"http://{self.ip}:{self.port}")
        # while starting:
        #     try:
        #         client.generate(prompt="test")
        #         starting = False
        #     except requests.exceptions.ConnectionError:
        #         pass
        #     time.sleep(1)
        # current_process = psutil.Process(self.process.pid)
        # self.child_processes = current_process.children(recursive=True)

    # def __del__(self):
    #     self.process.send_signal(signal.SIGTERM)
    #     for process in self.child_processes:
    #         process.send_signal(signal.SIGTERM)

    @app.post("/generate_stream")
    async def generate_stream(self, request: GenerateStream) -> StreamingResponse:
        client = Client(f"http://{self.ip}:{self.port}")
        gen = generate_stream_text(client, **request.dict())
        return StreamingResponse(gen, status_code=200, media_type="text/plain")


# num_gpus = 1
# app = TextGenerationInferenceDeployment.options(
#     ray_actor_options={"num_gpus": num_gpus}
# ).bind(model_id="Salesforce/codegen-350M-multi", num_shard=num_gpus)