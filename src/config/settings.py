import os
from pydantic_settings import BaseSettings
from pydantic import AnyUrl


class Settings(BaseSettings):
    # Application
    APP_NAME: str = "SGB Backend Madeira"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False

    # Database - Supabase / PostgreSQL
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/sgb_db"

    # JWT
    SECRET_KEY: str = "change-me-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    # CORS
    ALLOWED_ORIGINS: list[str] = ["*"]

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
