from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PORT: int = 8080
    DEBUG: bool = False

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
