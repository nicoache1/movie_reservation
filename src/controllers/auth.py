import logging

from src.api.v1.schemas.auth import SessionToken
from src.core.crypto import create_access_token, get_password_hash, verify_password
from src.core.exceptions import AuthException
from src.repositories.user import UserRepository


class AuthController:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def register_user(self, email: str, password: str) -> None:
        password_hash = get_password_hash(password)
        self.user_repository.create_user(email, password_hash)

    def login_user(self, email: str, password: str) -> SessionToken:
        user = self.user_repository.get_user_by_email(email)
        if not user or not verify_password(password, user.password_hash):
            logging.error("Invalid credentials")
            raise AuthException()

        access_token = create_access_token({"sub": user.email})
        return SessionToken(
            access_token=access_token,
            token_type="bearer",
        )
