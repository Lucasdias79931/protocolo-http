from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    UPLOAD_DIR: str = "uploads"

    model_config = SettingsConfigDict(
        extra='ignore',
        env_file='.env',
        env_file_encoding='utf-8'
    )

settings = Settings()

class Settings:
    UPLOAD_DIR = "uploads"

settings = Settings()