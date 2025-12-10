from fastapi import FastAPI
from app.routers import conversion_router

def create_app():
    app = FastAPI()

    app.include_router(conversion_router.router)

    return app