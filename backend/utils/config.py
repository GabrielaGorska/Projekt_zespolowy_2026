from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings and environment variables."""
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str = "localhost"
    DB_PORT: int = 3306
    DB_NAME: str

    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    RESET_TOKEN_EXPIRE_MINUTES: int = 60

    # Base URL for links in emails (e.g. http://localhost:3000)
    FRONTEND_URL: str = "http://localhost:3000"

    # SMTP (optional - emails are logged when SMTP is not configured)
    SMTP_HOST: str = ""
    SMTP_PORT: int = 587
    SMTP_USER: str = ""
    SMTP_PASSWORD: str = ""
    SMTP_FROM: str = "noreply@lswis.local"
    SMTP_USE_TLS: bool = True

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @property
    def smtp_enabled(self) -> bool:
        # When false, services/email.py logs messages instead of sending
        return bool(self.SMTP_HOST and self.SMTP_FROM)


settings = Settings()
