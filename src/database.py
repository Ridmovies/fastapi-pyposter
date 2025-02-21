from typing import Annotated

from fastapi import Depends
from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from src.config import settings

if settings.MODE == "TEST":
    DATABASE_URL = settings.TEST_DATABASE_URL
    # to fix RuntimeError: Task <Task pending name='Task-4'
    DATABASE_PARAMS = {"poolclass": NullPool}
else:
    DATABASE_URL = settings.DATABASE_URL
    DATABASE_PARAMS = {}

async_engine = create_async_engine(DATABASE_URL, **DATABASE_PARAMS, echo=True)
async_session = async_sessionmaker(async_engine, expire_on_commit=False)

# Dependency
async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session

SessionDep = Annotated[AsyncSession, Depends(get_session)]