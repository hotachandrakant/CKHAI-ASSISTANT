from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


class UploadResponse(BaseModel):
    message: str
    filename: str
    chunks_created: int
    collection: str


class QueryRequest(BaseModel):
    question: str = Field(..., min_length=3, max_length=1000)
    collection: Optional[str] = None
    top_k: Optional[int] = Field(default=5, ge=1, le=20)


class SourceDocument(BaseModel):
    page_content: str
    source: str
    page: Optional[int] = None


class QueryResponse(BaseModel):
    answer: str
    sources: List[SourceDocument]
    question: str
    model: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class HealthResponse(BaseModel):
    status: str
    version: str
    environment: str
