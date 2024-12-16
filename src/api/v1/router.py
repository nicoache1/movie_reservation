from fastapi import APIRouter

from src.api.v1.routers import auth, movie

v1_router = APIRouter()
v1_router.include_router(auth.router, prefix="/auth")
v1_router.include_router(movie.router, prefix="/movies")
