from unittest.mock import MagicMock

import pytest

from src.controllers.movie import MovieController
from src.models.movie import Movie
from src.repositories.movie import MovieRepository


@pytest.fixture
def mock_repo():
    """mock of MovieRepository."""
    return MagicMock(spec=MovieRepository)


@pytest.fixture
def movie_controller(mock_repo):
    """controller with repository mock."""
    return MovieController(movie_repository=mock_repo)


def test_get_movies_by_showtime(movie_controller, mock_repo):

    fake_showtime_id = 123
    fake_movies = [Movie(id=1, title="Movie A"), Movie(id=2, title="Movie B")]
    mock_repo.get_all_movies_by_showtime.return_value = fake_movies

    result = movie_controller.get_movies_by_showtime(showtime_id=fake_showtime_id)

    mock_repo.get_all_movies_by_showtime.assert_called_once_with(
        showtime_id=fake_showtime_id
    )

    assert result == fake_movies
