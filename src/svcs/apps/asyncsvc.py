from apps.routers.async_jobs import router
from fastapi import FastAPI
from ray import serve

batch_app = FastAPI()
batch_app.include_router(router)


@serve.deployment
@serve.ingress(batch_app)
class ServeBatch:
    def __init__(self) -> None:
        self.somevar = "namaste"

    @batch_app.post("/hello")
    def hello(self):
        return {"resp": self.somevar}
