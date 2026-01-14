import os
import logging
from app.core.settings import get_settings


def setup_logging():
    settings = get_settings()

    logging.basicConfig(
        level=getattr(logging, settings.LOG_LEVEL, logging.INFO),
        format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
        force=True,
    )
