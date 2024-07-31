
from datetime import datetime, timedelta
from schemas.jwt import TokenDuration

SECRET_KEY = "secret"

def generate_access_token(username: str) -> str:
    expiration = datetime.utcnow() + timedelta(seconds=TokenDuration.ACCESS_TOKEN_EXPIRATION.value)
    return jwt.encode({"sub": username, "exp": expiration}, SECRET_KEY, algorithm="HS512")

def generate_refresh_token(username: str) -> str:
    expiration = datetime.utcnow() + timedelta(seconds=TokenDuration.REFRESH_TOKEN_EXPIRATION.value)
    return jwt.encode({"sub": username, "exp": expiration}, SECRET_KEY, algorithm="HS512")

def get_username_from_token(token: str) -> str:
    return jwt.decode(token, SECRET_KEY, algorithms=["HS512"])["sub"]

def validate_token(token: str) -> bool:
    try:
        jwt.decode(token, SECRET_KEY, algorithms=["HS512"])
        return True
    except jwt.ExpiredSignatureError:
        return False
    except jwt.InvalidTokenError:
        return False
