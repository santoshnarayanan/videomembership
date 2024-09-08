from pydantic import Field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    keyspace: str = Field(..., alias='ASTRADB_KEYSPACE')


    class Config:
        env_file = '.env'


def get_settings():
    return Settings()