from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from src.config import settings

# DATABASE_URL = "postgresql+asyncpg://postgres:root@localhost:5432/pyposter"
DATABASE_URL = settings.DATABASE_URL

async_engine = create_async_engine(DATABASE_URL, echo=True)
async_session = async_sessionmaker(async_engine, expire_on_commit=False)

# Dependency
async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session

SessionDep = Annotated[AsyncSession, Depends(get_session)]