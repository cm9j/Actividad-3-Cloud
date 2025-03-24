from app.files.domain.controllers.list_files_controller import ListFilesController
from app.files.persistence.postgres.file_repository_postgres import FileRepositoryPostgres


def get_list_files_controller() -> ListFilesController:
    return ListFilesController(FileRepositoryPostgres())
