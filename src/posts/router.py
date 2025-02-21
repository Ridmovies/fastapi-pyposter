from fastapi import APIRouter
from sqlalchemy import select

from src.database import SessionDep
from src.posts.models import Post

post_router = APIRouter()


@post_router.get("")
async def get_all_posts(session: SessionDep):
    stmt = select(Post)
    result = await session.execute(stmt)
    users = result.scalars().all()
    return users