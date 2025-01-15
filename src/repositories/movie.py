from typing import List

from sqlmodel import Session, select

from src.models.movie import Movie
from src.models.showtime import Showtime


class MovieRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all_movies_by_showtime(self, showtime_id: int) -> List[Movie]:
        statement = (
            select(Movie)
            .join(
                Showtime,
            )
            .where(Showtime.id == showtime_id)
        )

        # Another way to write the same query using ORM Relationships without JOIN
        # statement = (
        #   select(Movie)
        #   .where(
        #       Movie.showtimes.any(id=showtime_id)
        #   )
        # )
        #
        # To know more about JOINS in SQLMODEL check out the official documentation:
        # https://sqlmodel.tiangolo.com/tutorial/connect/read-connected-data/#join-tables-in-sqlmodel

        return self.db.exec(statement).all()
