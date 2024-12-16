from pydantic import BaseModel


class AuthRequest(BaseModel):
    email: str
    password: str


class SessionToken(BaseModel):
    access_token: str
    token_type: str
