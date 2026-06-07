import structlog
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_chroma import Chroma
import chromadb
from app.config import get_settings
 
logger = structlog.get_logger()
settings = get_settings()
 
SUPPORTED_EXTENSIONS = {".pdf", ".docx", ".txt"}
 
 
def get_loader(file_path: str):
    ext = Path(file_path).suffix.lower()
    if ext == ".pdf":
        return PyPDFLoader(file_path)
    elif ext == ".docx":
        return Docx2txtLoader(file_path)
    elif ext == ".txt":
        return TextLoader(file_path, encoding="utf-8")
    raise ValueError(f"Unsupported file type: {ext}")
 
 
def get_chroma_client():
    return chromadb.HttpClient(
        host=settings.chroma_host,
        port=settings.chroma_port,
    )
 
 
def get_vector_store(collection_name: str = None) -> Chroma:
    collection = collection_name or settings.chroma_collection
    embeddings = OllamaEmbeddings(
        model="nomic-embed-text",
        base_url="http://localhost:11434",
    )
    chroma_client = get_chroma_client()
    return Chroma(
        client=chroma_client,
        collection_name=collection,
        embedding_function=embeddings,
    )
 
 
async def ingest_document(file_path: str, collection_name: str = None) -> int:
    logger.info("ingestion_started", file=file_path)
    loader = get_loader(file_path)
    documents = loader.load()
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=settings.chunk_size,
        chunk_overlap=settings.chunk_overlap,
        length_function=len,
        separators=["\n\n", "\n", " ", ""],
    )
    chunks = splitter.split_documents(documents)
    for chunk in chunks:
        chunk.metadata["source"] = Path(file_path).name
    vector_store = get_vector_store(collection_name)
    vector_store.add_documents(chunks)
    logger.info("ingestion_complete", file=file_path, chunks=len(chunks))
    return len(chunks)
