from sqlmodel import Session, select

from src.models.user import User


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, email: str, hashed_password: str) -> User:
        new_user = User(
            email=email,
            password_hash=hashed_password,
        )

        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user

    def get_user_by_email(self, email: str) -> User | None:
        statement = select(User).where(User.email == email)
        return self.db.exec(statement).first()
