from typing import List

from fastapi import APIRouter, Depends

from app.authentication.domain.dependencies.verify_token import verify_token
from app.files.dependency_injection.domain.list_files_controller_factory import (
    get_list_files_controller,
)
from app.files.domain.controllers.list_files_controller import ListFilesController
from app.files.domain.schemas import FileResponse

router = APIRouter()

@router.get("/files", response_model=List[FileResponse])
async def list_files(
    user_id: int = Depends(verify_token),
    controller: ListFilesController = Depends(get_list_files_controller)
):
    files = await controller.execute(user_id)
    return [FileResponse(**file.__dict__) for file in files]

