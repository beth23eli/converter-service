import os
import logging
import logging.config
from datetime import datetime
from pathlib import Path
import yaml
from .settings import ServiceConfig


def setup_logger(log_level="DEBUG", name: str = None):
    config = ServiceConfig()
    try:
        with open(config.LOGGING_YAML, "r") as f:
            log_cfg = yaml.safe_load(f)

        log_cfg["root"]["level"] = config.LOG_LEVEL

        logging.config.dictConfig(log_cfg)

        logger = logging.getLogger(name) if name else logging.getLogger()
        logger.info("Logging configured")
        return logger
    except Exception as e:
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger(name) if name else logging.getLogger()
        logger.error(f"Failed to load logging configuration: {e}")
        return logger


def get_logger(name: str = None):
    return logging.getLogger(name)