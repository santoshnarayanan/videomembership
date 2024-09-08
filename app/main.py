from fastapi import FastAPI
from . import config

app = FastAPI()
settings = config.get_settings()

@app.get("/")
def homepage():
    return {"hello":"world","keyspace":settings.keyspace} # json data --> REST API
