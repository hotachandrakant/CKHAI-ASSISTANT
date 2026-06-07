"""
Services package
----------------
Core business logic for the RAG pipeline:
- ingestion  : load → chunk → embed → store in ChromaDB
- retrieval  : vector search → LLM generation → structured response
"""

from app.services import ingestion, retrieval

__all__ = ["ingestion", "retrieval"]
