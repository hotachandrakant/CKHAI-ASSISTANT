import os
import pytest

# Set dummy env vars so app can import without a real .env file during tests
os.environ.setdefault("OPENAI_API_KEY", "sk-test-dummy-key-for-testing")
os.environ.setdefault("API_KEY", "test-key")
os.environ.setdefault("CHROMA_HOST", "localhost")
os.environ.setdefault("CHROMA_PORT", "8000")
os.environ.setdefault("APP_ENV", "test")
