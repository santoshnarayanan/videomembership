import datetime
from app import config
from jose import ExpiredSignatureError, jwt

from .models import User

settings = config.get_settings()


def authenticate_user(email, password):
    # step 1
    try:
        user_obj = User.objects.get(email=email)
    except Exception as e:
        user_obj = None
        if not user_obj.verify_password(password):
            return None
        token = user_obj

def login(user_obj, expires=5):
    # step 2
    raw_data = {
        "user_id": f"{user_obj.user_id}",
        "role": "admin", 
        "exp" : datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(seconds=expires)
    }
    return jwt.encode(raw_data, settings.secret_key, algorithm=settings.jwt_algorithm)

def verify_user(token):
    token_decoded = None
    verified = False
    try:
        data = jwt.decode(token, settings.secret_key, algorithm=settings.jwt_algorithm)
    except ExpiredSignatureError as e:
        print (e)
    except:
        pass
    if 'user_id' not in data:
        return None
    return data
