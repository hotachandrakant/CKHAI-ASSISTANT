import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app

HEADERS = {"X-API-Key": "test-key"}


@pytest.mark.asyncio
async def test_health_endpoint():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        resp = await client.get("/health")
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "healthy"
    assert "version" in data


@pytest.mark.asyncio
async def test_upload_requires_auth():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        resp = await client.post("/api/v1/upload")
    assert resp.status_code == 403


@pytest.mark.asyncio
async def test_upload_rejects_unsupported_type():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        resp = await client.post(
            "/api/v1/upload",
            headers=HEADERS,
            files={"file": ("image.png", b"fake content", "image/png")},
        )
    assert resp.status_code == 415


@pytest.mark.asyncio
async def test_swagger_docs_accessible():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        resp = await client.get("/docs")
    assert resp.status_code == 200
