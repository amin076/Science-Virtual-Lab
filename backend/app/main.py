"""
main.py — entry point for Science Virtual Lab backend.
Creates and configures the FastAPI application instance.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings  # our config file
from app.api.routes import health
# Create the FastAPI app
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    debug=settings.DEBUG,
    description="Backend service for scientific experiment simulations."
)

# CORS (Cross-Origin Resource Sharing) setup
# Allows frontend (Next.js app) to access backend API during development
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(health.router, prefix="/health", tags=["Health"])

# Root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to Science Virtual Lab API"}
