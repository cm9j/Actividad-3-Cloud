from pydantic import BaseModel


class UserRequest(BaseModel):
    email: str
    password: str

class UserLoginRequest(BaseModel):
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    email: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
