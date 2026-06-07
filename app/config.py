from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    openai_api_key: str = ""
    api_key: str
    chroma_host: str = "localhost"
    chroma_port: int = 8000
    chroma_collection: str = "documents"
    chunk_size: int = 1000
    chunk_overlap: int = 200
    embedding_model: str = "text-embedding-3-small"
    llm_model: str = "gpt-4o"
    max_retrieved_docs: int = 5
    app_env: str = "development"
    log_level: str = "INFO"
    gemini_api_key: str = ""

    class Config:
        env_file = ".env"
        case_sensitive = False


@lru_cache()
def get_settings() -> Settings:
    return Settings()