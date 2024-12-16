from enum import Enum

from pydantic import PostgresDsn
from pydantic_settings import BaseSettings

DB_USER = "dev"
DB_PASSWORD = "dev"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "movie_reservation"


class Settings(BaseSettings):
    database_url: PostgresDsn


settings = Settings(
    database_url=f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
