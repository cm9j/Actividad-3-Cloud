from typing import List

from app.files.domain.bo.file_bo import FileBO
from app.files.domain.persistences.file_repository import FileRepository


class ListFilesController:
    def __init__(self, file_repository: FileRepository):
        self.file_repository = file_repository

    async def execute(self, user_id: int) -> List[FileBO]:
        return await self.file_repository.get_all_by_user(user_id)
