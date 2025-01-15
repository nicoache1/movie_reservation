from datetime import datetime

import pytest
from sqlalchemy.orm import sessionmaker
from sqlmodel import Session, SQLModel, create_engine

from src.models.movie import Movie
from src.models.showtime import Showtime
from src.repositories.showtime import ShowtimeRepository


@pytest.fixture(scope="function")
def db_session():

    engine = create_engine("sqlite:///:memory:", echo=True)

    SQLModel.metadata.create_all(engine)

    SessionLocal = sessionmaker(
        autocommit=False, autoflush=False, bind=engine, class_=Session
    )
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@pytest.fixture
def showtime_repository(db_session):
    return ShowtimeRepository(db=db_session)


@pytest.fixture
def seed_data(db_session):
    movie = Movie(id=1, title="Test Movie", description="Test description")
    db_session.add(movie)
    db_session.commit()

    showtime1 = Showtime(id=1, movie_id=1, start_time=datetime(2024, 12, 19, 10, 0, 0))
    showtime2 = Showtime(id=2, movie_id=1, start_time=datetime(2024, 12, 19, 14, 0, 0))
    db_session.add(showtime1)
    db_session.add(showtime2)
    db_session.commit()

    return movie


def test_get_showtimes_by_movie_id(showtime_repository, db_session, seed_data):
    movie_id = seed_data.id

    showtimes = showtime_repository.get_showtimes_by_movie_id(movie_id)

    assert len(showtimes) == 2
    assert showtimes[0].movie_id == movie_id
    assert showtimes[1].movie_id == movie_id
    assert showtimes[0].start_time == datetime(2024, 12, 19, 10, 0, 0)
    assert showtimes[1].start_time == datetime(2024, 12, 19, 14, 0, 0)


def test_get_showtimes_by_movie_raw(showtime_repository, db_session, seed_data):
    movie_id = seed_data.id

    showtimes = showtime_repository.get_showtimes_by_movie_raw(movie_id)

    assert len(showtimes) == 2
    assert showtimes[0].movie_id == movie_id
    assert showtimes[1].movie_id == movie_id
    assert showtimes[0].start_time == datetime(2024, 12, 19, 10, 0, 0)
    assert showtimes[1].start_time == datetime(2024, 12, 19, 14, 0, 0)
