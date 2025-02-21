from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env')

    MODE: Literal["DEV", "TEST", "PROD"]
    DATABASE_URL: str
    TEST_DATABASE_URL: str


settings = Settings()

