"""
Tests package
-------------
Async test suite using pytest + httpx.

Run with:
    pytest tests/ -v

Tests cover:
- Authentication enforcement (403 without X-API-Key)
- Input validation (422 for bad question length, invalid top_k)
- File type rejection (415 for unsupported formats)
- Health endpoint (200 OK)
- Swagger docs accessibility (200 OK)

Note: Tests use dummy env vars from conftest.py — no real
OpenAI key or running ChromaDB instance required.
"""
