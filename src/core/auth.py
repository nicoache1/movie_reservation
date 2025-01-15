from typing import Any

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from src.core.crypto import decode_access_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_current_user(token: str = Depends(oauth2_scheme)) -> Any:

    token = decode_access_token(token)

    return token
