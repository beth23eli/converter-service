from fastapi import APIRouter, status
import logging

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/health", status_code=status.HTTP_200_OK)
def health():
    logger.info("Health endpoint accessed")
    return {"status": "ok"}
