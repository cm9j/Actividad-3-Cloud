from app.files.domain.controllers.upload_file_controller import UploadFileController
from app.files.persistence.postgres.file_repository_postgres import FileRepositoryPostgres


def get_upload_file_controller() -> UploadFileController:
    return UploadFileController(file_repository=FileRepositoryPostgres())
