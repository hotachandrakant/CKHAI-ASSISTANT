"""
Core package
------------
Shared infrastructure used across the app:
- auth : API key verification middleware (X-API-Key header)
"""

from app.core import auth

__all__ = ["auth"]
