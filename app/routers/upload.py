import os
import tempfile
from fastapi import APIRouter, UploadFile, File, Depends, HTTPException, status
from pathlib import Path
from app.services.ingestion import ingest_document, SUPPORTED_EXTENSIONS
from app.core.auth import verify_api_key
from app.models.schemas import UploadResponse
from app.config import get_settings

router = APIRouter(prefix="/api/v1", tags=["ingestion"])
settings = get_settings()

MAX_FILE_SIZE_MB = 50


@router.post("/upload", response_model=UploadResponse, dependencies=[Depends(verify_api_key)])
async def upload_document(
    file: UploadFile = File(...),
    collection: str = None,
):
    """Upload and ingest a document (PDF, DOCX, or TXT) into the vector store."""
    ext = Path(file.filename).suffix.lower()
    if ext not in SUPPORTED_EXTENSIONS:
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail=f"File type '{ext}' not supported. Accepted: {sorted(SUPPORTED_EXTENSIONS)}",
        )

    contents = await file.read()
    if len(contents) > MAX_FILE_SIZE_MB * 1024 * 1024:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail=f"File exceeds {MAX_FILE_SIZE_MB}MB limit.",
        )

    # Write to a temp file so loaders can work with a real path
    with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as tmp:
        tmp.write(contents)
        tmp_path = tmp.name

    try:
        chunks = await ingest_document(tmp_path, collection)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        os.unlink(tmp_path)

    return UploadResponse(
        message="Document ingested successfully",
        filename=file.filename,
        chunks_created=chunks,
        collection=collection or settings.chroma_collection,
    )
