
from functools import wraps
from fastapi import HTTPException, Request
from .auth import verify_user
from .exceptions import LoginRequiredException

def login_required(func):
    @wraps(func)
    def wrapper(request:Request, *args, **kwargs):
        session_token= request.cookies.get("session_id")
        print(session_token)
        user_session = verify_user(session_token)
        print(user_session)
        if user_session is None:
            raise LoginRequiredException(status_code=401) 
        return func(request, *args, **kwargs)
    return wrapper