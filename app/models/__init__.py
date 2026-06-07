"""
Models package
--------------
Pydantic schemas for all API request and response bodies:
- UploadResponse  : returned after a document is ingested
- QueryRequest    : incoming question payload
- QueryResponse   : answer + source citations + metadata
- SourceDocument  : a single retrieved chunk with page/source info
- HealthResponse  : health check response
"""

from app.models.schemas import (
    UploadResponse,
    QueryRequest,
    QueryResponse,
    SourceDocument,
    HealthResponse,
)

__all__ = [
    "UploadResponse",
    "QueryRequest",
    "QueryResponse",
    "SourceDocument",
    "HealthResponse",
]
