from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, HTTPException, status

from src.api.v1.schemas.auth import AuthRequest
from src.controllers.auth import AuthController
from src.core.container import Container
from src.core.exceptions import AuthException

router = APIRouter()


@router.post("/register", status_code=status.HTTP_201_CREATED)
@inject
def register_user(
    auth_request: AuthRequest,
    auth_controller: AuthController = Depends(Provide[Container.auth_controller]),
) -> None:
    try:
        return auth_controller.register_user(
            auth_request.email,
            auth_request.password,
        )
    except AuthException as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


@router.post("/login")
@inject
def login_user(
    auth_request: AuthRequest,
    auth_controller: AuthController = Depends(Provide[Container.auth_controller]),
):
    try:
        return auth_controller.login_user(
            auth_request.email,
            auth_request.password,
        )
    except AuthException as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )
