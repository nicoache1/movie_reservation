from typing import List

from sqlalchemy import text
from sqlmodel import Session, select

from src.models.movie import Movie
from src.models.showtime import Showtime


class ShowtimeRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_showtimes_by_movie_id(self, movie_id: int) -> List[Showtime]:
        statement = (
            select(Showtime)
            .where(Showtime.movie_id == movie_id)
            .join(
                Movie,
            )
        )

        return self.db.exec(statement).all()

    def get_showtimes_by_movie_raw(self, movie_id: int) -> List[Showtime]:
        result = self.db.execute(
            text(
                """
            SELECT showtime.*
            FROM showtime
            INNER JOIN movie ON showtime.movie_id = movie.id
            WHERE movie.id = :movie_id
            """
            ),
            {"movie_id": movie_id},
        )
        rows = result.fetchall()
        return [
            Showtime.model_validate(row if isinstance(row, dict) else row._asdict())
            for row in rows
        ]
