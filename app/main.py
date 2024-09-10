import pathlib
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from cassandra.cqlengine.management import sync_table

from . import config, db
from .users.models import User

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
    context = {"request": request, "abc": 123}
    return templates.TemplateResponse("home.html", context)


@app.get("/login", response_class=HTMLResponse)
def login_get_view(request: Request):
    return templates.TemplateResponse("auth/login.html", {"request": request})


@app.post("/login", response_class=HTMLResponse)
def login_post_view(request: Request, email: str = Form(...), password: str = Form(...)):
    print(email, password)
    return templates.TemplateResponse("auth/login.html", {"request": request})


@app.get("/signup", response_class=HTMLResponse)
def signup_get_view(request: Request):
    return templates.TemplateResponse("auth/signup.html", {"request": request})


@app.post("/signup", response_class=HTMLResponse)
def signup_post_view(request: Request, email: str = Form(...), 
                        password: str = Form(...), password_confirm: str = Form(...),
                        
                    ):
    print(email, password)
    return templates.TemplateResponse("auth/signup.html", {"request": request})



@app.get("/users")
def users_list_view():
    q = User.objects.all().limit(10)
    return list(q)
