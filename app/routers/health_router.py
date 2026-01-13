from fastapi import APIRouter, status
from app.core.logging import logger

router = APIRouter()


@router.get("/health", status_code=status.HTTP_200_OK)
def health():
    logger.info("Health endpoint accessed")
    return {"status": "ok"}
