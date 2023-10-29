import time
from typing import Generator

import requests
from pydantic import BaseModel
from ray import serve
from starlette.requests import Request
from starlette.responses import StreamingResponse


@serve.deployment
class StreamingResponder:
    def generate_numbers(self, max: int) -> Generator[str, None, None]:
        for i in range(max):
            yield str(i)
            time.sleep(0.1)

    async def __call__(self, request: Request) -> StreamingResponse:
        data = await request.json()
        max = data["max_new_tokens"]
        gen = self.generate_numbers(max)
        return StreamingResponse(gen, status_code=200, media_type="text/plain")
