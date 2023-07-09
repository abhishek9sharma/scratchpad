import time
from typing import Generator

import requests
from starlette.responses import StreamingResponse
from starlette.requests import Request

from ray import serve


@serve.deployment
class StreamingResponder:
    def generate_numbers(self, max: int) -> Generator[str, None, None]:
        for i in range(max):
            yield str(i)
            time.sleep(0.1)

    def __call__(self, request: Request) -> StreamingResponse:
        max = request.query_params.get("max", "25")
        gen = self.generate_numbers(int(max))
        return StreamingResponse(gen, status_code=200, media_type="text/plain")


#serve.run(StreamingResponder.bind())