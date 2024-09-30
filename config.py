from pydantic import BaseSettings


class Settings(BaseSettings):
    MYGES_LOGIN: str
    MYGES_PASSWORD: str

    DESTINATION_EMAIL: str

    MAILJET_API_KEY: str
    MAILJET_SECRET_KEY: str
    MAILJET_SENDER_EMAIL: str

    class Config:
        env_file = '.env'


settings = Settings()
