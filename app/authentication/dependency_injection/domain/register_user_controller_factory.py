from app.authentication.domain.controllers.register_user_controller import RegisterUserController
from app.authentication.persistence.postgres.user_repository_postgres import UserRepositoryPostgres


def get_register_user_controller() -> RegisterUserController:
    user_repo = UserRepositoryPostgres()
    return RegisterUserController(user_repo)
