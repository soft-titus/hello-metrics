"""
Main FastAPI application for the Sudoku API
"""

from fastapi import FastAPI

from app.helpers.logger import logger
from app.routes.health_routes import router as health_router
from app.routes.hello_routes import router as hello_router


app = FastAPI(title="Hello")

app.include_router(health_router)
logger.info("Health router registered at /health")

app.include_router(hello_router)
logger.info("Hello router registered at /hello")

logger.info("FastAPI Hello initialized")
