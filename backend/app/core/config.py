import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "API Monitor SaaS"
    SQLALCHEMY_DATABASE_URI: str = os.getenv("DATABASE_URL")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "supersecret")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60*24
    SMTP_HOST: str = os.getenv("SMTP_HOST")
    SMTP_PORT: int = int(os.getenv("SMTP_PORT", 587))
    SMTP_USER: str = os.getenv("SMTP_USER")
    SMTP_PASS: str = os.getenv("SMTP_PASS")
    CORS_ORIGINS: list = os.getenv("CORS_ORIGINS", "*").split(",")
    REDIS_BROKER_URL: str = os.getenv("REDIS_BROKER_URL", "redis://localhost:6379/0")

settings = Settings()