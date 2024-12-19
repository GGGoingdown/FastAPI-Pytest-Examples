import time
import asyncio

from fastapi import FastAPI
from src import utils


app = FastAPI()



@app.get("/health")
async def health():
    result = {}
    result["status"] = "ok"
    result["version"] = "0.1.0"

    utils.some_complex_function()
    return {"status": "ok"}



@app.get("/greeting")
async def greeting(name: str = "John Doe"):
    greeting_message = utils.generate_greeting(name)
    return {"message": greeting_message}


@app.get("/sync")
async def sync():
    utils.long_running_task()
    return {"status": "ok"}


@app.get("/sync-in-thread")
def sync_in_thread():
    utils.long_running_task()
    return {"status": "ok"}


@app.get("/async")
async def async_():
    await utils.async_long_running_task()
    return {"status": "ok"}


@app.get("/sequential")
async def sequential():
    t1 = time.perf_counter()
    for _ in range(3):
        await utils.async_long_running_task(sleep_time=1)
    t2 = time.perf_counter()
    return {"total_time": t2 - t1}


@app.get("/concurrent")
async def concurrent():
    t1 = time.perf_counter()
    tasks = [utils.async_long_running_task(sleep_time=1) for _ in range(3)]
    await asyncio.gather(*tasks)
    t2 = time.perf_counter()

    return {"total_time": t2 - t1}