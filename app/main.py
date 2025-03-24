from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.security import OAuth2PasswordBearer
from tortoise.contrib.fastapi import register_tortoise

from app.authentication.api.router import router as auth_router
from app.files.api.router import router as files_router

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

app = FastAPI()


# Incluir routers
app.include_router(auth_router, prefix="/auth")
app.include_router(files_router, prefix="/files")

# Inicializar Tortoise ORM
register_tortoise(
    app,
    db_url="postgres://postgres:postgres@db:5432/fastapi_storage",
    modules={"models": ["app.authentication.models", "app.files.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema


    openapi_schema = get_openapi(
        title="FastAPI Storage",
        version="1.0.0",
        description="API con autenticación JWT",
        routes=app.routes,
    )

    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method["security"] = [{"BearerAuth": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi
