from fastapi import APIRouter
from sqlalchemy import text

from src.database import SessionDep

dev_router = APIRouter()

@dev_router.get("")
async def check_db_connection(session: SessionDep):
    result = await session.execute(text("SELECT 1"))
    return {"message": result}