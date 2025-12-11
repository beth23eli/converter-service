from fastapi import FastAPI
import os
import logging
from app.routers import conversion_router, health_router

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()

logging.basicConfig(
    level=LOG_LEVEL,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
)

logger = logging.getLogger(__name__)

def create_app():
    app = FastAPI()

    app.include_router(health_router.router)
    app.include_router(conversion_router.router)

    return app