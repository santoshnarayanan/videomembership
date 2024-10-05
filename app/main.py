from multiprocessing import context
import pathlib
import json
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from cassandra.cqlengine.management import sync_table
from pydantic import ValidationError
# from requests import session

from . import db, utils
from .shortcuts import render, redirect
from .users.models import User
from .users.schemas import (UserSignupSchema, UserLoginSchema)


# BASE_DIR= pathlib.Path(__file__).resolve() # path of main.py
BASE_DIR = pathlib.Path(__file__).resolve().parent  # app directory
TEMPLATE_DIR = BASE_DIR / "templates"  # path of templates directory

app = FastAPI()
templates = Jinja2Templates(directory=str(TEMPLATE_DIR))
DB_SESSION = None  # Setting global variable
# settings = config.get_settings()


@app.on_event("startup")
def on_startup():
    # triggered when fastapi starts
    print("hello world")
    global DB_SESSION
    DB_SESSION = db.get_session()
    sync_table(User)


@app.get("/", response_class=HTMLResponse)
def homepage(request: Request):
    context = { "abc": 123}
    return render(request, "home.html", context)


@app.get("/login", response_class=HTMLResponse)
def login_get_view(request: Request):
    session_id= request.cookies.get("session_id")
    return render(request, "auth/login.html", {"logged_in": session_id is not None})


@app.post("/login", response_class=HTMLResponse)
def login_post_view(request: Request, email: str = Form(...), password: str = Form(...)):
    
    # print(email, password)
    raw_data = {
        "email": email,
        "password": password
    }
    data, errors = utils.valid_schema_data_or_error(raw_data, UserLoginSchema)
    context = {"data": data, "errors": errors}
    if len(errors) > 0:
        return render(request, "auth/login.html", context, status_code=400)
    return redirect("/", cookies=data)


@app.get("/signup", response_class=HTMLResponse)
def signup_get_view(request: Request):
    return render(request, "auth/signup.html")


@app.post("/signup", response_class=HTMLResponse)
def signup_post_view(request: Request, email: str = Form(...),
                     password: str = Form(...), password_confirm: str = Form(...),

                     ):

    raw_data = {
        "email": email,
        "password": password,
        "password_confirm": password_confirm
    }
    data, errors = utils.valid_schema_data_or_error(raw_data, UserSignupSchema)
    if len(errors) > 0:
        return render(request, "auth/signup.html", context, status_code=400)
    return redirect("/login")


@app.get("/users")
def users_list_view():
    q = User.objects.all().limit(10)
    return list(q)
