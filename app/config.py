from app import BaseSettings, Options, SettingsConfigDict

class Settings(BaseSettings):
    poc_secret_key_token : str
    poc_expiration_token_time: int = 30
    poc_algorithm_jwt_token: str = "HS256"
    poc_selenium_headless: str = "S"

    model_config = SettingsConfigDict(env_file=" .env")

settings = Settings()

options = Options()
if settings.poc_selenium_headless == "S":
    options.add_argument("--headless=new")