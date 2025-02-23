from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        env_nested_delimiter='.',
    )

    database_url: str

    jwt_algorithm: str
    jwt_secret_key: str
    jwt_access_token_expire: int
    jwt_refresh_token_expire: int


settings = Settings()
