from fastapi import FastAPI
from app.routers import conversion_router, health_router
from app.core.logging import setup_logger

def create_app():
    app = FastAPI()

    setup_logger("app")

    app.include_router(health_router.router)
    app.include_router(conversion_router.router)

    return app