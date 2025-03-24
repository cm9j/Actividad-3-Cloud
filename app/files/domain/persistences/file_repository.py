from abc import ABC, abstractmethod

from app.files.domain.bo.file_bo import FileBO


class FileRepository(ABC):
    @abstractmethod
    async def create(self, file: FileBO) -> FileBO:
        pass

    @abstractmethod
    async def get_all(self) -> list[FileBO]:
        pass
