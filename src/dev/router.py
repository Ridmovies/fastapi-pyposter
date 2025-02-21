from fastapi import APIRouter
from sqlalchemy import text

from src.database import SessionDep, async_engine
from src.models import Base

dev_router = APIRouter()

@dev_router.get("")
async def check_db_connection(session: SessionDep):
    result = await session.execute(text("SELECT 1"))
    return {"message": result}


@dev_router.delete("")
async def restart_db():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)