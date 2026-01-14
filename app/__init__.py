from fastapi import FastAPI
from app.core.logging import setup_logging
from app.routers import conversion_router, health_router

def create_app():
    setup_logging()
    
    app = FastAPI()

    app.include_router(health_router.router)
    app.include_router(conversion_router.router)

    return app