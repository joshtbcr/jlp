from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_USER: str
    DB_PASS: str
    DB_HOST: str
    DB_NAME: str
    SECRET_KEY: str
    NOMBRE_EMPRESA: str
    NOMBRE_ARCHIVO_CUENTA_EXCEL: str

    class Config:
        env_file = ".env"

settings = Settings()
