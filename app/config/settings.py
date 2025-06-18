from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PORT: int = 8080
    DEBUG: bool = False
    MONGO_URI: str = "mongodb://localhost:27017"
    MONGO_DB: str = "fastAPI"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
