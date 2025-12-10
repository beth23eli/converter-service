from fastapi import FastAPI
import os
import logging
from app.routers import conversion_router

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()

logging.basicConfig(
    level=LOG_LEVEL,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
)

logger = logging.getLogger(__name__)

def create_app():
    app = FastAPI()

    logger.info(f"App started with LOG_LEVEL={LOG_LEVEL}")
    logger.debug("DEBUG: km-to-miles endpoint called")

    app.include_router(conversion_router.router)

    return app