from app.authentication.domain.persistences.user_repository import UserRepository
from app.authentication.domain.services.jwt_service import create_access_token


class LoginUserController:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def execute(self, email: str, password: str) -> str | None:
        user = await self.user_repository.get_by_email(email)
        if not user or user.password != password:
            return None

        token = create_access_token({"sub": str(user.id)})
        return token

