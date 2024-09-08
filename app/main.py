from fastapi import FastAPI
from  cassandra.cqlengine.management import sync_table

from . import config, db
from .users.models import User

app = FastAPI()
DB_SESSION =None # Setting global variable
# settings = config.get_settings()

@app.on_event("startup")
def on_startup():
    # triggered when fastapi starts
    print("hello world")
    global DB_SESSION
    DB_SESSION = db.get_session()
    sync_table(User)


@app.get("/")
def homepage():
    return {
        "hello": "world",
        "keyspace": settings.keyspace,
        "db_id": settings.db_client_id,
        "db_secret": settings.db_client_secret
    }  # json data --> REST API
