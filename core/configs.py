from importlib.metadata import metadata
from sqlalchemy import MetaData
from sqlalchemy.orm import declarative_base
from pydantic import BaseSettings

class Settings(BaseSettings):
    """Configuraçoes gerais da aplicaçao"""
    API_V1_STR:  str = 'api/v1'
    DB_URL: str = 'mysql+pymysql://root:Janela2412#@localhost:3306/faculdade'
    DBBaseModel = declarative_base()


class Config: 
    case_sensitive = True


settings = Settings()