from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache
from pydantic import field_validator


class Settings(BaseSettings):
    LOG_LEVEL: str = "INFO"
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

    @field_validator("LOG_LEVEL")
    def validate_log_level(cls, level):
        valid_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
        if level not in valid_levels:
            raise ValueError(f"Invalid LOG_LEVEL: {level}. Must be one of {valid_levels}")
        return level

@lru_cache
def get_settings():
    return Settings()
