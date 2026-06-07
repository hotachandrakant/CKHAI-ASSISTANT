import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app

HEADERS = {"X-API-Key": "test-key"}


@pytest.mark.asyncio
async def test_query_requires_auth():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        resp = await client.post(
            "/api/v1/query",
            json={"question": "What is this about?"},
        )
    assert resp.status_code == 403


@pytest.mark.asyncio
async def test_query_rejects_too_short_question():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        resp = await client.post(
            "/api/v1/query",
            headers=HEADERS,
            json={"question": "hi"},
        )
    assert resp.status_code == 422


@pytest.mark.asyncio
async def test_query_rejects_too_long_question():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        resp = await client.post(
            "/api/v1/query",
            headers=HEADERS,
            json={"question": "x" * 1001},
        )
    assert resp.status_code == 422


@pytest.mark.asyncio
async def test_query_rejects_invalid_top_k():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        resp = await client.post(
            "/api/v1/query",
            headers=HEADERS,
            json={"question": "What are the findings?", "top_k": 50},
        )
    assert resp.status_code == 422
