import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_get_all_posts(client: AsyncClient):
    response = await client.get("/posts")
    assert response.status_code == 200
    assert len(response.json()) == 0
