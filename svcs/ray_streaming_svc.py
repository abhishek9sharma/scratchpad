import time
from typing import Generator

import requests
from starlette.responses import StreamingResponse
from starlette.requests import Request
from text_generation import Client
from ray import serve

from pydantic import BaseModel

def generate_stream_text(client: Client, *args, **kwargs):
    for response in client.generate_stream(*args, **kwargs):
        if not response.token.special:
            yield response.token.text
            time.sleep(0.01)

from pydantic import BaseModel
from typing import List, Optional


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


@serve.deployment
class StreamingResponder:
    def generate_numbers(self, max: int) -> Generator[str, None, None]:
        for i in range(max):
            yield str(i)
            time.sleep(0.1)

    async def  __call__(self, request: Request) -> StreamingResponse:
        #max = request.query_params.get("max", "25")
        #gen = self.generate_numbers(25)
        payload1 = await request.json()
        
        payload = {"prompt":"def add(a,b):","do_sample":False,"max_new_tokens":100, "return_full_text":False, "watermark":False} 
        client = Client("http://127.0.0.1:8080")
        gen = generate_stream_text(client, **payload1)
        return  StreamingResponse(gen, status_code=200, media_type="text/plain")


#serve.run(StreamingResponder.bind())