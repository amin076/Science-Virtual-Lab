"""
config.py — centralized configuration for Science Virtual Lab backend.
All environment variables and project settings are defined here.
"""

from pydantic import BaseSettings
from typing import List

class Settings(BaseSettings):
    PROJECT_NAME: str = "Science Virtual Lab API"
    VERSION: str = "0.1.0"
    DEBUG: bool = True

    # Allowed origins for CORS (frontend URLs)
    BACKEND_CORS_ORIGINS: List[str] = ["*"]  # TODO: restrict later to Vercel domain

    # Optional: Firebase or DB configs (will be used in later phases)
    FIREBASE_PROJECT_ID: str | None = None
    FIREBASE_API_KEY: str | None = None

    class Config:
        env_file = ".env"  # Load environment variables from .env file

# Instantiate settings for global use
settings = Settings()
