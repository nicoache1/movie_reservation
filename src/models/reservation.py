import json
from datetime import datetime, timezone
from enum import Enum
from typing import List, Optional

from sqlalchemy import JSON, Column
from sqlmodel import Field, Relationship, SQLModel

from src.models.showtime import Showtime
from src.models.user import User


class ReservationStatus(str, Enum):
    CONFIRMED = "confirmed"
    CANCELED = "canceled"
    PENDING = "pending"


class ReservationBase(SQLModel):
    user_id: int = Field(foreign_key="user.id")
    showtime_id: int = Field(foreign_key="showtime.id")
    seats_reserved: Optional[List[str]] = Field(
        default_factory=list, sa_column=Column(JSON)
    )
    status: ReservationStatus = Field(default=ReservationStatus.CONFIRMED)
    created_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
    updated_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    @property
    def seats_reserved_json(self):
        return json.dumps(self.seats_reserved)

    @seats_reserved_json.setter
    def seats_reserved_json(self, value: str):
        self.seats_reserved = json.loads(value)


class Reservation(ReservationBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user: User = Relationship(back_populates="reservations")
    showtime: Showtime = Relationship(back_populates="reservations")
