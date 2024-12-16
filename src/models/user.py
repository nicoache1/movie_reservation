from datetime import datetime, timezone
from enum import Enum
from typing import TYPE_CHECKING, List, Optional

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .reservation import Reservation


class UserRole(str, Enum):
    USER = "user"
    ADMIN = "admin"


class UserBase(SQLModel):
    email: str = Field(index=True, unique=True)
    password_hash: str
    role: str = Field(default="user")
    created_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
    updated_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )


class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    reservations: List["Reservation"] = Relationship(back_populates="user")
