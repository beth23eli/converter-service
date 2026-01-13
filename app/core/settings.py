import os
from typing import Optional
from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

class ServiceConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="allow")
    ENV: str = Field(default="dev", description="Environment: dev, staging, prod")
    LOG_LEVEL: str = Field(default="DEBUG", description="Logging level")
    LOGGING_YAML: Path = Field(default=Path("logging.yaml"))

    @field_validator("LOG_LEVEL")
    def validate_log_level(cls, level):
        valid_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
        if level not in valid_levels:
            raise ValueError(f"Invalid LOG_LEVEL: {level}. Must be one of {valid_levels}")
