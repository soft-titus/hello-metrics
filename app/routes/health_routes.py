"""
Health router.
"""

from fastapi import APIRouter
from app.helpers.logger import logger

router = APIRouter(
    tags=["Health"],
    responses={500: {"description": "Internal Server Error"}},
)


@router.get(
    "/health",
    summary="Service health check",
    description="Check if the service is running and responsive.",
    response_description="Returns the current status of the service",
)
def health():
    """Health check endpoint."""
    logger.info("Health endpoint hit")

    return {
        "status": "ok",
    }
