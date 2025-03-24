from app.authentication.domain.controllers.login_user_controller import LoginUserController
from app.authentication.persistence.postgres.user_repository_postgres import UserRepositoryPostgres


def get_login_user_controller() -> LoginUserController:
    user_repository = UserRepositoryPostgres()
    return LoginUserController(user_repository)

