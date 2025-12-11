from fastapi import FastAPI
from app.routers import conversion_router, health_router

def create_app():
    app = FastAPI()

    app.include_router(health_router.router)
    app.include_router(conversion_router.router)

    return app