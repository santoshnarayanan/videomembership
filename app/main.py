from fastapi import FastAPI
from . import config

app = FastAPI()
settings = config.get_settings()


@app.get("/")
def homepage():
    return {
        "hello": "world",
        "keyspace": settings.keyspace,
        "db_id": settings.db_client_id,
        "db_secret": settings.db_client_secret
    }  # json data --> REST API
