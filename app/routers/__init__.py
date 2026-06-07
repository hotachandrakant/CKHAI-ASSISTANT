"""
Routers package
---------------
Contains all FastAPI route handlers:
- upload  : POST /api/v1/upload  — ingest documents into ChromaDB
- query   : POST /api/v1/query   — ask questions, get cited answers
"""

from app.routers import upload, query

__all__ = ["upload", "query"]
