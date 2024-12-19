import time 
import asyncio

def long_running_task(sleep_time: int = 10):
    print("Start long running task")
    time.sleep(sleep_time)
    print("End long running task")
    return "ok"


async def async_long_running_task(sleep_time: int = 10):
    print("Start long running task")
    await asyncio.sleep(sleep_time)
    print("End long running task")
    return "ok"


def some_complex_function():
    record = {}
    record["name"] = "John Doe"
    record["age"] = 30
    return record


def generate_greeting(name: str):
    return f"Hello, {name}"