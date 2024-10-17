from pydantic import BaseSettings


class Settings(BaseSettings):
    MYGES_LOGIN: str
    MYGES_PASSWORD: str

    TELEGRAM_BOT_TOKEN: str
    TELEGRAM_CHANNEL_ID: str

    class Config:
        env_file = '.env'


settings = Settings()
