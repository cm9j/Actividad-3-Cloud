from abc import ABC, abstractmethod

from app.authentication.domain.bo.user_bo import UserBO


class UserRepository(ABC):
    @abstractmethod
    async def get_by_email(self, email: str) -> UserBO | None:
        pass

    @abstractmethod
    async def create(self, user: UserBO) -> UserBO:
        pass

    @abstractmethod
    async def get_last_external_id(self) -> int:
        pass
