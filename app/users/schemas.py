
# from requests import session
from . import auth
from .models import User
from pydantic import BaseModel, EmailStr, SecretStr, model_validator, field_validator
from  cassandra.cqlengine.management import sync_table


class UserLoginSchema(BaseModel):
    email: EmailStr
    password: SecretStr
    session_id: str = None

    [model_validator]
    def validate_user(cls, values):
        err_msg = "Invalid credentials.Please try again"
        email = values.get("email") or None
        password = values.get("password") or None
        # user = auth.authenticate_user(email, password)
        if email is None or password is None:
            raise ValueError(err_msg)
        password = password.get_secret_value()
        user_obj = auth.authenticate_user(email, password)
        if user_obj is None:
            raise ValueError(err_msg)
        token = auth.login(user_obj)
        return {"session_id": token}
    

class UserSignupSchema(BaseModel):
    email: EmailStr
    password: SecretStr
    password_confirm: SecretStr

    @field_validator("email")
    def email_available(cls, v, values, **kwargs):
        q = User.objects.filter(email=v)
        if q.count() != 0:
            raise ValueError("Email is not available")
        return v
    
    @field_validator("password_confirm")
    def passwords_match(cls, v, values, **kwargs):
        password = values.get('password')
        password_confirm = v
        if password != password_confirm:
            raise ValueError("Passwords do not match")
        return v
    