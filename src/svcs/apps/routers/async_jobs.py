# https://www.phind.com/search?cache=ahmhuhq8qa85ro1n2nscb9cq

import asyncio
from http import HTTPStatus
from typing import Dict
from uuid import UUID, uuid4

import uvicorn
from fastapi import APIRouter, BackgroundTasks, FastAPI
from pydantic import BaseModel, Field
import ray
import time

class Job(BaseModel):
    uid: UUID = Field(default_factory=uuid4)
    status: str = "in_progress"
    progress: int = 0
    result: int = None


app = FastAPI()
# prefix_router = APIRouter(prefix="/my_server_path")
router = APIRouter()
jobs: Dict[UUID, Job] = {}  # Dict as job storage


@ray.remote
async def long_task(queue: asyncio.Queue, param: int):
    for i in range(1, param):  # do work and return our progress
        await asyncio.sleep(10)
        await queue.put(i)
    await queue.put(None)


async def start_new_task(uid: UUID, param: int) -> None:
    queue = asyncio.Queue()
    task = asyncio.create_task(long_task(queue, param))

    while progress := await queue.get():  # monitor task progress
        jobs[uid].progress = progress

    jobs[uid].status = "complete"

# @ray.remote
# def some_task():
#     time.sleep(10)
#     return 1

# async def await_obj_ref():clear
#     await some_task.remote()
#     await asyncio.wait([some_task.remote()])

# asyncio.run(await_obj_ref())


@router.post("/new_task/{param}", status_code=HTTPStatus.ACCEPTED)
async def task_handler(background_tasks: BackgroundTasks, param: int):
    new_task = Job()
    jobs[new_task.uid] = new_task
    background_tasks.add_task(start_new_task, new_task.uid, param)
    return new_task


@router.get("/task/{uid}/status")
async def status_handler(uid: UUID):
    return jobs[uid]


@router.get("/hello")
async def hello():
    return {"resp": "hello"}
