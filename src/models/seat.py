from typing import Optional

from sqlmodel import Field, Relationship, SQLModel

from .showtime import Showtime


class SeatBase(SQLModel):
    showtime_id: int = Field(foreign_key="showtime.id")
    seat_number: str
    is_reserved: bool = Field(default=False)


class Seat(SeatBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    showtime: Showtime = Relationship(back_populates="seats")
