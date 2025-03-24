from fastapi import APIRouter, Depends, HTTPException

from app.authentication.dependency_injection.domain.login_user_controller_factory import (
    get_login_user_controller,
)
from app.authentication.dependency_injection.domain.register_user_controller_factory import (
    get_register_user_controller,
)
from app.authentication.domain.controllers.login_user_controller import LoginUserController
from app.authentication.domain.controllers.register_user_controller import RegisterUserController
from app.authentication.domain.schemas import TokenResponse, UserRequest, UserResponse
from app.authentication.domain.services.current_user_service import get_current_user

router = APIRouter()

@router.post("/register", response_model=UserResponse)
async def register_user(
    data: UserRequest,
    controller: RegisterUserController = Depends(get_register_user_controller),
):
    user = await controller.execute(email=data.email, password=data.password)
    return UserResponse(id=user.id, email=user.email)

@router.post("/login", response_model=TokenResponse)
async def login_user(
    data: UserRequest,
    controller: LoginUserController = Depends(get_login_user_controller),
):
    token = await controller.execute(email=data.email, password=data.password)
    if not token:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    return TokenResponse(access_token=token)


@router.get("/me")
async def get_me(user_data: dict = Depends(get_current_user)):
    return {"user_id": user_data.get("sub")}
