from datetime import datetime, timezone
from typing import TYPE_CHECKING, List, Optional

from sqlmodel import Field, Relationship, SQLModel

from .movie import Movie

if TYPE_CHECKING:
    from .reservation import Reservation
    from .seat import Seat


class ShowtimeBase(SQLModel):
    movie_id: int = Field(foreign_key="movie.id")
    start_time: datetime
    seats_capacity: int = Field(default=100, ge=1, le=100)
    created_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
    updated_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )


class Showtime(ShowtimeBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    movie: Movie = Relationship(back_populates="showtimes")
    reservations: List["Reservation"] = Relationship(back_populates="showtime")
    seats: List["Seat"] = Relationship(back_populates="showtime")
