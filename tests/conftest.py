import pytest 
import time
import pytest_asyncio
from httpx import AsyncClient, ASGITransport

from src.main import app 

@pytest.fixture(autouse=True)
def timer_function_scope():
    start = time.time()
    yield
    print(' Time cost: {:.3f}s'.format(time.time() - start))


@pytest_asyncio.fixture()
async def client():
    async with AsyncClient(transport=ASGITransport(app), base_url="http://test") as client:
        yield client