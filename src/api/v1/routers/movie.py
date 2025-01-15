from typing import List

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, HTTPException, status

from src.controllers.showtime import ShowtimeController
from src.core.container import Container
from src.core.exceptions import AuthException
from src.models.showtime import Showtime

router = APIRouter()


@router.get("/{movie_id}/showtimes", response_model=List[Showtime])
@inject
def get_showtimes_by_movie_id(
    movie_id: int,
    showtime_controller: ShowtimeController = Depends(
        Provide[Container.showtime_controller]
    ),
):
    try:
        return showtime_controller.get_showtimes_by_movie_id(
            movie_id=movie_id,
        )
    except AuthException as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


@router.get("/{movie_id}/showtimes/raw", response_model=List[Showtime])
@inject
def get_showtimes_by_movie_raw(
    movie_id: int,
    showtime_controller: ShowtimeController = Depends(
        Provide[Container.showtime_controller]
    ),
):
    return showtime_controller.get_showtimes_by_movie_raw(
        movie_id=movie_id,
    )
