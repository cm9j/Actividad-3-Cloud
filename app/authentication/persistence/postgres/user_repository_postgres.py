from app.authentication.domain.bo.user_bo import UserBO
from app.authentication.domain.persistences.user_repository import UserRepository
from app.authentication.models import User  # modelo Tortoise


class UserRepositoryPostgres(UserRepository):
    async def get_by_email(self, email: str) -> UserBO | None:
        user = await User.get_or_none(email=email)
        if not user:
            return None
        return UserBO(
            id=user.id,
            email=user.email,
            password=user.password,
            external_id=user.external_id,
        )

    async def create(self, user: UserBO) -> UserBO:
        new_user = await User.create(
            email=user.email,
            password=user.password,
            external_id=user.external_id
        )
        return UserBO(
            id=new_user.id,
            email=new_user.email,
            password=new_user.password,
            external_id=new_user.external_id,
        )

    async def get_last_external_id(self) -> int:
        last_user = await User.all().order_by("-external_id").first()
        return last_user.external_id if last_user else 0
