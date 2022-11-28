import pytest
from httpx import AsyncClient
from datetime import datetime

from main import app

pytestmark = pytest.mark.anyio



async def test_app_has_correct_format():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")

    assert response.status_code == 200
    assert 'time' in response.json()
    assert datetime_valid(response.json()['time'])


def datetime_valid(datetime_string):
    try:
        datetime.fromisoformat(datetime_string)
    except ValueError:
        return False
    return True


@pytest.fixture
def anyio_backend():
    return 'asyncio'
