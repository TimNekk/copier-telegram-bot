from __future__ import annotations

from pydantic import DirectoryPath, NonNegativeFloat, PositiveInt, SecretStr, computed_field
from pydantic_settings import BaseSettings as PydanticBaseSettings
from pydantic_settings import SettingsConfigDict


class BaseSettings(PydanticBaseSettings):
    model_config = SettingsConfigDict(extra="allow")


class BotSettings(BaseSettings):
    token: SecretStr
    default_locale: str
    rate_limit: NonNegativeFloat


class FileLogSettings(BaseSettings):
    name: str
    directory: DirectoryPath
    level: str


class PostgresSettings(BaseSettings):
    host: str
    port: PositiveInt
    name: str
    user: str
    password: SecretStr

    @computed_field
    @property
    def url(self) -> SecretStr:
        return SecretStr(
            f"postgresql+psycopg://{self.user}:{self.password.get_secret_value()}@{self.host}:{self.port}/{self.name}",
        )


class RedisSettings(BaseSettings):
    port: PositiveInt


class Settings(BaseSettings):
    bot: BotSettings
    file_log: FileLogSettings
    postgres: PostgresSettings
    redis: RedisSettings

    model_config = SettingsConfigDict(env_nested_delimiter="__")
