import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_health(mocker, client: AsyncClient):
    mocker.patch('src.utils.some_complex_function', return_value={"name": "John Doe", "age": 30})
    response = await client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}



@pytest.mark.asyncio
async def test_greeting(mocker, client: AsyncClient):
    greeting_message = "Hello, John Doe"
    mocker.patch('src.utils.generate_greeting', return_value=greeting_message)
    response = await client.get("/greeting")
    assert response.status_code == 200
    assert response.json() == {"message": greeting_message}