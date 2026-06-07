import structlog
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from app.routers import upload, query
from app.models.schemas import HealthResponse
from app.config import get_settings

settings = get_settings()
structlog.configure(wrapper_class=structlog.make_filtering_bound_logger(20))
logger = structlog.get_logger()

limiter = Limiter(key_func=get_remote_address)

app = FastAPI(
    title="RAG Document Q&A API",
    description="Production-grade Retrieval-Augmented Generation API — upload docs, ask questions.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload.router)
app.include_router(query.router)


@app.get("/health", response_model=HealthResponse, tags=["system"])
async def health():
    """Health check endpoint for Docker and load balancer probes."""
    return HealthResponse(
        status="healthy",
        version="1.0.0",
        environment=settings.app_env,
    )


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error("unhandled_exception", path=request.url.path, error=str(exc))
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error. Check server logs."},
    )


logger.info("app_startup", env=settings.app_env, model=settings.llm_model)
