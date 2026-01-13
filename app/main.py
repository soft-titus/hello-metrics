"""
Main FastAPI application for the Sudoku API
"""

from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

from app.helpers.logger import logger
from app.routes.health_routes import router as health_router
from app.routes.hello_routes import router as hello_router


app = FastAPI(title="Hello")

Instrumentator(
    excluded_handlers=["/health"],
    should_group_status_codes=False,
    should_ignore_untemplated=True,
).instrument(app)

app.include_router(health_router)
logger.info("Health router registered at /health")

app.include_router(hello_router)
logger.info("Hello router registered at /hello")

logger.info("FastAPI Hello initialized")
