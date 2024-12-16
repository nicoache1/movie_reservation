from dependency_injector import containers, providers

from src.controllers.auth import AuthController
from src.controllers.showtime import ShowtimeController
from src.core.database import get_db
from src.repositories.showtime import ShowtimeRepository
from src.repositories.user import UserRepository


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "src.api.v1.routers.auth",
            "src.api.v1.routers.movie",
            "src.controllers.auth",
            "src.controllers.showtime",
            "src.repositories.user",
            "src.repositories.showtime",
        ]
    )

    # DB
    db_session = providers.Resource(get_db)

    # Repositories
    user_repository = providers.Factory(
        UserRepository,
        db=db_session,
    )
    showtime_repository = providers.Factory(
        ShowtimeRepository,
        db=db_session,
    )

    # Controllers
    showtime_controller = providers.Factory(
        ShowtimeController, showtime_repository=showtime_repository
    )
    auth_controller = providers.Factory(
        AuthController,
        user_repository=user_repository,
    )
