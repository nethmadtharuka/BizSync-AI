from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    
    APP_NAME: str = "BizSync AI API"
    DATABASE_URL: str = "postgresql+psycopg://bizsync:bizsync@localhost:5432/bizsync"
    
    WHATSAPP_VERIFY_TOKEN: str = "dev_verify_token"
    WHATSAPP_ACCESS_TOKEN: str = "dev_access_token"
    WHATSAPP_PHONE_NUMBER_ID: str = "000000000000000"


settings = Settings()