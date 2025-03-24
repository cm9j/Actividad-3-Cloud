from app.authentication.domain.bo.user_bo import UserBO
from app.authentication.domain.persistences.user_repository import UserRepository


class RegisterUserController:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def execute(self, email: str, password: str) -> UserBO | None:
        existing_user = await self.user_repository.get_by_email(email)
        if existing_user:
            return None  # Usuario ya existe

        last_external_id = await self.user_repository.get_last_external_id()
        new_user = UserBO(
            email=email,
            password=password,  # en el futuro cifrado
            external_id=last_external_id + 1
        )
        created_user = await self.user_repository.create(new_user)
        return created_user
