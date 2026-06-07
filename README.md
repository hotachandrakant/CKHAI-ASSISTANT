# RAG Document Q&A System

A **production-grade Retrieval-Augmented Generation (RAG) API** built for your ML developer portfolio.

Upload PDFs, DOCX, or TXT files — then ask natural language questions. Answers are grounded strictly in your documents, with source citations returned alongside every answer.

---

## Tech stack

| Layer | Technology |
|---|---|
| API | FastAPI + Uvicorn (async) |
| RAG pipeline | LangChain |
| Vector store | ChromaDB (persistent Docker volume) |
| LLM | OpenAI GPT-4o |
| Embeddings | text-embedding-3-small |
| Auth | API key via `X-API-Key` header |
| Container | Docker + Docker Compose |
| Tests | pytest + httpx |
| Logging | structlog (structured JSON) |

---

## Project structure

```
rag-qa-system/
├── app/
│   ├── main.py              # FastAPI app, middleware, global error handler
│   ├── config.py            # All settings loaded from env vars
│   ├── routers/
│   │   ├── upload.py        # POST /api/v1/upload
│   │   └── query.py         # POST /api/v1/query
│   ├── services/
│   │   ├── ingestion.py     # Document load → chunk → embed → store pipeline
│   │   └── retrieval.py     # Vector search + LLM answer generation (RAG chain)
│   ├── core/
│   │   └── auth.py          # API key authentication middleware
│   └── models/
│       └── schemas.py       # Pydantic request/response models
├── tests/
│   ├── conftest.py          # Test env setup (dummy API keys)
│   ├── test_upload.py
│   └── test_query.py
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
├── pytest.ini
├── .env.example
├── .gitignore
└── requirements.txt
```

---

## Setup — step by step

### Prerequisites
- Docker Desktop installed and running
- Python 3.11+ (for local dev only)
- An OpenAI API key from https://platform.openai.com

### Step 1 — Clone and configure

```bash
git clone https://github.com/YOUR_USERNAME/rag-qa-system
cd rag-qa-system
cp .env.example .env
```

Now open `.env` and fill in **two required values**:

```env
OPENAI_API_KEY=sk-your-real-openai-key
API_KEY=pick-any-secret-string-you-want
```

Generate a strong `API_KEY` with:
```bash
openssl rand -hex 32
```

### Step 2 — Run with Docker

```bash
cd docker
docker-compose up --build
```

This starts two containers:
- `api` — your FastAPI app on `http://localhost:8080`
- `chromadb` — the vector database on `http://localhost:8001`

Vectors are stored in a Docker volume (`chroma_data`) — they persist across restarts.

### Step 3 — Verify it's running

```bash
curl http://localhost:8080/health
```

Expected response:
```json
{"status": "healthy", "version": "1.0.0", "environment": "production"}
```

Also open the Swagger UI: http://localhost:8080/docs

---

## Usage

### Upload a document

```bash
curl -X POST http://localhost:8080/api/v1/upload \
  -H "X-API-Key: your-api-key" \
  -F "file=@path/to/your/document.pdf"
```

Response:
```json
{
  "message": "Document ingested successfully",
  "filename": "document.pdf",
  "chunks_created": 38,
  "collection": "documents"
}
```

Supported formats: `.pdf`, `.docx`, `.txt` (max 50 MB each)

### Ask a question

```bash
curl -X POST http://localhost:8080/api/v1/query \
  -H "X-API-Key: your-api-key" \
  -H "Content-Type: application/json" \
  -d '{"question": "What are the key findings?"}'
```

Response:
```json
{
  "answer": "The key findings include three main areas...",
  "sources": [
    {
      "page_content": "The study found that...",
      "source": "document.pdf",
      "page": 4
    }
  ],
  "question": "What are the key findings?",
  "model": "gpt-4o",
  "timestamp": "2024-01-15T10:30:00"
}
```

### Optional query parameters

```json
{
  "question": "Summarise the methodology",
  "collection": "documents",
  "top_k": 8
}
```

- `collection` — query a specific ChromaDB collection (default: `documents`)
- `top_k` — number of chunks to retrieve (1–20, default: 5)

---

## API reference

| Method | Endpoint | Auth | Description |
|---|---|---|---|
| GET | `/health` | No | Health check |
| GET | `/docs` | No | Swagger UI |
| GET | `/redoc` | No | ReDoc docs |
| POST | `/api/v1/upload` | Yes | Upload + ingest a document |
| POST | `/api/v1/query` | Yes | Ask a question |

All protected endpoints require the `X-API-Key` header.

---

## Local development (without Docker)

```bash
# 1. Create and activate virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run ChromaDB separately (still needs Docker for this)
docker run -p 8001:8000 chromadb/chroma:latest

# 4. Set env vars for local run
export OPENAI_API_KEY=sk-your-key
export API_KEY=dev-secret
export CHROMA_HOST=localhost
export CHROMA_PORT=8001

# 5. Start the API with hot reload
uvicorn app.main:app --reload --port 8080
```

---

## Run tests

```bash
# Activate venv first
source venv/bin/activate

pip install -r requirements.txt
pytest tests/ -v
```

Tests don't hit OpenAI or ChromaDB — they test auth, validation, and routing only.

---

## Environment variables

| Variable | Default | Required | Description |
|---|---|---|---|
| `OPENAI_API_KEY` | — | Yes | OpenAI API key |
| `API_KEY` | — | Yes | Your chosen API key for auth |
| `CHROMA_HOST` | `chromadb` | No | ChromaDB hostname |
| `CHROMA_PORT` | `8000` | No | ChromaDB port |
| `CHROMA_COLLECTION` | `documents` | No | Default collection name |
| `CHUNK_SIZE` | `1000` | No | Characters per chunk |
| `CHUNK_OVERLAP` | `200` | No | Overlap between chunks |
| `EMBEDDING_MODEL` | `text-embedding-3-small` | No | OpenAI embedding model |
| `LLM_MODEL` | `gpt-4o` | No | OpenAI chat model |
| `MAX_RETRIEVED_DOCS` | `5` | No | Chunks retrieved per query |
| `APP_ENV` | `development` | No | Environment label |
| `LOG_LEVEL` | `INFO` | No | Log verbosity |

---

## How the RAG pipeline works

```
User uploads PDF
       |
       v
  PyPDFLoader loads pages
       |
       v
  RecursiveCharacterTextSplitter
  chunks text (1000 chars, 200 overlap)
       |
       v
  OpenAI text-embedding-3-small
  converts each chunk to a vector
       |
       v
  ChromaDB stores vectors + metadata
       |
  User asks question
       |
       v
  Question is embedded (same model)
       |
       v
  MMR search finds top-k similar chunks
       |
       v
  GPT-4o generates answer from context
       |
       v
  Answer + source citations returned
```

---

## Deploy to production (Vercel / Railway / Render)

For cloud deployment, set these environment variables in your cloud provider's dashboard instead of `.env`:

- `OPENAI_API_KEY`
- `API_KEY`
- `CHROMA_HOST` (point to a hosted ChromaDB or use Pinecone instead)

For Vercel specifically, use `vercel.json` to route requests to your Docker container. Railway and Render support Docker Compose directly.

---

## Built by Chandrakant Hota
- GitHub: github.com/hotachandrakant
- LinkedIn: linkedin.com/in/chandrakant-hota-6757a939b
