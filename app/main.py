"""
Main FastAPI application for the Sudoku API
"""

from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

from app.helpers.logger import logger
from app.routes.health_routes import router as health_router
from app.routes.hello_routes import router as hello_router


app = FastAPI(title="Hello")

app.include_router(health_router)
logger.info("Health router registered at /health")

app.include_router(hello_router)
logger.info("Hello router registered at /hello")

Instrumentator(
    excluded_handlers=[
        "/health",
        "/metrics",
    ],
    should_group_status_codes=False,
    should_ignore_untemplated=True,
).instrument(app).expose(
    app,
    endpoint="/metrics",
    include_in_schema=False,
)
logger.info("Prometheus metrics exposed at /metrics")

logger.info("FastAPI Hello initialized")
