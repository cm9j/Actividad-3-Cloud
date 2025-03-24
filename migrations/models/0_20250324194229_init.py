from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "users" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "email" VARCHAR(255) NOT NULL UNIQUE,
    "password" VARCHAR(255) NOT NULL,
    "external_id" INT NOT NULL UNIQUE
);
CREATE TABLE IF NOT EXISTS "files" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "filename" VARCHAR(255) NOT NULL,
    "content_type" VARCHAR(100) NOT NULL,
    "path" VARCHAR(255) NOT NULL,
    "owner_id" INT NOT NULL
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
