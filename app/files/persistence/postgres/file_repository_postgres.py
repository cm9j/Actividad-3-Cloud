from typing import List

from app.files.domain.bo.file_bo import FileBO
from app.files.domain.persistences.file_repository import FileRepository
from app.files.models import File  # modelo Tortoise


class FileRepositoryPostgres(FileRepository):
    async def get_all_by_user(self, user_id: int) -> List[FileBO]:
        files = await File.filter(user_id=user_id).all()
        return [
            FileBO(
                id=file.id,
                user_id=file.user_id,
                filename=file.filename,
                uploaded_at=file.uploaded_at
            ) for file in files
        ]
