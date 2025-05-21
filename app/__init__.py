from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi


from pydantic_settings import BaseSettings, SettingsConfigDict

from selenium.webdriver.chrome.options import Options