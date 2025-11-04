"""
health.py — simple route for checking server health.
This endpoint helps ensure the backend is alive and responding.
"""

from fastapi import APIRouter

# Create a router instance
router = APIRouter()

@router.get("/")
def health_check():
    """
    Health check endpoint.
    Returns a simple JSON response to confirm the server is running.
    """
    return {"status": "ok"}
