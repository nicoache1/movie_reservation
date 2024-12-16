from typing import List

from src.models.movie import Movie
from src.repositories.movie import MovieRepository


class MovieController:
    def __init__(self, movie_repository: MovieRepository):
        self.movie_repository = movie_repository

    def get_movies_by_showtime(self, showtime_id: int) -> List[Movie]:
        return self.movie_repository.get_all_movies_by_showtime(
            showtime_id=showtime_id,
        )
