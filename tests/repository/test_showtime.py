from datetime import datetime
from unittest.mock import MagicMock

import pytest
from sqlmodel import Session

from src.models.showtime import Showtime
from src.repositories.showtime import ShowtimeRepository


@pytest.fixture
def mock_db_session():
    mock_session = MagicMock(spec=Session)
    return mock_session


@pytest.fixture
def showtime_repository(mock_db_session):
    return ShowtimeRepository(db=mock_db_session)


def test_get_showtimes_by_movie_id(showtime_repository, mock_db_session):
    movie_id = 1

    showtimes = [
        Showtime(id=1, movie_id=movie_id, start_time=datetime(2024, 12, 19, 10, 0, 0)),
        Showtime(id=2, movie_id=movie_id, start_time=datetime(2024, 12, 19, 14, 0, 0)),
    ]

    mock_db_session.exec.return_value.all.return_value = showtimes

    result = showtime_repository.get_showtimes_by_movie_id(movie_id)

    assert result == showtimes
    mock_db_session.exec.assert_called_once()


def test_get_showtimes_by_movie_raw(showtime_repository, mock_db_session):
    movie_id = 1
    start_time = datetime(2024, 12, 19, 10, 0, 0)
    raw_showtimes = [
        {"id": 1, "movie_id": movie_id, "start_time": start_time},
        {"id": 2, "movie_id": movie_id, "start_time": datetime(2024, 12, 19, 14, 0, 0)},
    ]

    mock_db_session.execute.return_value.fetchall.return_value = raw_showtimes

    result = showtime_repository.get_showtimes_by_movie_raw(movie_id)

    assert len(result) == 2
    assert result[0].id == movie_id
    assert result[0].start_time == start_time
    mock_db_session.execute.assert_called_once()
