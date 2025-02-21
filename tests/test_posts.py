import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_get_all_posts(client: AsyncClient):
    response = await client.get("/posts")
    assert response.status_code == 200
    assert len(response.json()) == 0


@pytest.mark.asyncio
async def test_create_post(client: AsyncClient):
    json_data = {"content": "test_string"}
    response = await client.post("/posts", json=json_data)
    assert response.status_code == 201
    assert response.json() == {"id": 1, "content": "test_string"}


@pytest.mark.asyncio
async def test_delete_post_404(client: AsyncClient):
    response = await client.get("/posts")
    assert len(response.json()) == 1

    post_id = 999999
    response = await client.delete(f"/posts/{post_id}")
    assert response.status_code == 404

    response = await client.get("/posts")
    assert len(response.json()) == 1


@pytest.mark.asyncio
async def test_delete_post_204(client: AsyncClient):
    response = await client.get("/posts")
    assert len(response.json()) == 1

    post_id = 1
    response = await client.delete(f"/posts/{post_id}")
    assert response.status_code == 204

    response = await client.get("/posts")
    assert len(response.json()) == 0


@pytest.mark.asyncio
async def test_update_post_200(client: AsyncClient):
    json_data = {"content": "test_string"}
    response = await client.post("/posts", json=json_data)
    assert response.status_code == 201
    assert response.json() == {"id": 2, "content": "test_string"}

    post_id = 2
    json_data = {"content": "test_string_updated"}
    response = await client.put(f"/posts/{post_id}", json=json_data)
    assert response.status_code == 200
    assert response.json() == {"id": 2, "content": "test_string_updated"}





