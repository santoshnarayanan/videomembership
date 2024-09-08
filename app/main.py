from fastapi import FastAPI
from  cassandra.cqlengine.management import sync_table
from . import config

app = FastAPI()
# settings = config.get_settings()

@app.on_event("startup")
def on_startup():
    # triggered when fastapi starts
    print("hello world")


@app.get("/")
def homepage():
    return {
        "hello": "world",
        "keyspace": settings.keyspace,
        "db_id": settings.db_client_id,
        "db_secret": settings.db_client_secret
    }  # json data --> REST API
