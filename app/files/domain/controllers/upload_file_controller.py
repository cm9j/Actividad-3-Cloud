from app.files.domain.bo.file_bo import FileBO
from app.files.domain.persistences.file_repository import FileRepository


class UploadFileController:
    def __init__(self, file_repository: FileRepository):
        self.file_repository = file_repository

    async def execute(self, name: str, content: bytes) -> FileBO:
        file_bo = FileBO(name=name, content=content)
        created_file = await self.file_repository.create(file_bo)
        return created_file
