"""Module for load settings form `.env` or if server running with parameter
`dev` from `.env.dev`"""

from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic.types import SecretStr


class Settings(BaseSettings):
    """Server settings.

    Formed from `.env` or `.env.dev`.
    """
    model_config = SettingsConfigDict(
        case_sensitive=True,
        env_file=Path(__file__).parent.parent / ".env",
        env_file_encoding="utf-8",
        extra="allow",
    )
    #: str: Rabbitmq host.
    RABBITMQ_HOST: str

    #: str: Postgresql user.
    RABBITMQ_DEFAULT_USER: str
    #: SecretStr: Postgresql password.
    RABBITMQ_DEFAULT_PASS: SecretStr

    #: str: Selenium host.
    SELENIUM_HOST: str


SETTINGS = Settings()
