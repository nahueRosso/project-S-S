from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    app_name: str = "RIR API"
    app_version: str = "0.1.0"
    environment: str = "development"

    model_config = SettingsConfigDict(env_prefix="RIR_", env_file=".env")


settings = Settings()
