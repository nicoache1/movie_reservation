from typing import List

from src.models.showtime import Showtime
from src.repositories.showtime import ShowtimeRepository


class ShowtimeController:
    def __init__(self, showtime_repository: ShowtimeRepository):
        self.showtime_repository = showtime_repository

    def get_showtimes_by_movie_id(self, movie_id: int) -> List[Showtime]:
        return self.showtime_repository.get_showtimes_by_movie_id(
            movie_id,
        )

    def get_showtimes_by_movie_raw(self, movie_id: int) -> List[Showtime]:
        return self.showtime_repository.get_showtimes_by_movie_raw(
            movie_id,
        )
