from lib2to3.pytree import convert
from fastapi import Depends, HTTPException
import jwt

from typing import Any

from pydantic import ValidationError
from core.config import settings
from datetime import date, datetime, timedelta
from passlib.context import CryptContext
from fastapi.security import HTTPBearer

reusable_oauth2 = HTTPBearer(
    scheme_name='Authorization'
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_access_token(username: str | Any) -> str:
    print(username)
    expire = datetime.utcnow() + timedelta(
        seconds=settings.ACCESS_TOKEN_EXPIRE_SECONDS
    )
    to_encode = {
        "exp": expire, "username": str(username)
    }
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.SECURITY_ALGORITHM)
    return encoded_jwt

def validate_token(http_authorization_credentials=Depends(reusable_oauth2)) -> str:
    """
    Decode JWT token to get username => return username
    """
    try:
        payload = jwt.decode(http_authorization_credentials.credentials, settings.SECRET_KEY, algorithms=[settings.SECURITY_ALGORITHM])
        if datetime.fromtimestamp(payload.get('exp')) < datetime.now():
            raise HTTPException(status_code=403, detail="Token expired")
        return payload.get('username')
    except(jwt.PyJWTError, ValidationError):
        raise HTTPException(
            status_code=403,
            detail=f"Could not validate credentials",
        )

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def verify_password_test(username, password):
    if username == 'admin' and password == 'admin':
        return True
    return False

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)