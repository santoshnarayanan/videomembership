import os
from pydantic import Field
from pydantic_settings import BaseSettings
from functools import lru_cache

# UserWarning: CQLENG_ALLOW_SCHEMA_MANAGEMENT environment variable is not set.
os.environ['CQLENG_ALLOW_SCHEMA_MANAGEMENT'] = "1"

class Settings(BaseSettings):
    keyspace: str = Field(..., alias='ASTRADB_KEYSPACE')
    db_client_id: str = Field(..., alias='ASTRADB_CLIENT_ID')
    db_client_secret: str = Field(..., alias='ASTRADB_CLIENT_SECRET')

    class Config:
        env_file = '.env'


@lru_cache
def get_settings():
    return Settings()