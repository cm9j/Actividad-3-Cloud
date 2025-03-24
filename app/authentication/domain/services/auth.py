from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from app.authentication.domain.services.jwt_service import verify_access_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

async def verify_token(token: str = Depends(oauth2_scheme)):
    payload = verify_access_token(token)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido o expirado",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return payload
