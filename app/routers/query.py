from fastapi import APIRouter, Depends, HTTPException, status
from app.services.retrieval import answer_question
from app.core.auth import verify_api_key
from app.models.schemas import QueryRequest, QueryResponse

router = APIRouter(prefix="/api/v1", tags=["query"])


@router.post("/query", response_model=QueryResponse, dependencies=[Depends(verify_api_key)])
async def query_documents(request: QueryRequest):
    """Ask a natural language question; get an answer grounded in your documents."""
    try:
        return await answer_question(
            question=request.question,
            collection_name=request.collection,
            top_k=request.top_k,
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Query failed: {str(e)}",
        )
