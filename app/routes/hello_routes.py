"""
Hello router.
"""

from fastapi import APIRouter
from app.helpers.logger import logger
from app.metrics import hello_requests_total

router = APIRouter(
    tags=["Hello"],  # Groups this endpoint under "Hello" in Swagger/OpenAPI UI
    responses={500: {"description": "Internal Server Error"}},
)


@router.get(
    "/hello",
    summary="Greeting endpoint",
    description="Returns a simple greeting message.",
    response_description="A dictionary containing a greeting message",
)
def hello():
    """Hello endpoint."""
    logger.info("Hello endpoint hit")

    hello_requests_total.inc()

    return {
        "message": "Hello",
    }
