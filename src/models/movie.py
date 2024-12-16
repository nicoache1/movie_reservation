from datetime import datetime, timezone
from typing import TYPE_CHECKING, List, Optional

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .showtime import Showtime


class MovieBase(SQLModel):
    title: str
    description: Optional[str] = None
    poster_url: Optional[str] = None
    created_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
    updated_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )


class Movie(MovieBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    showtimes: List["Showtime"] = Relationship(back_populates="movie")
