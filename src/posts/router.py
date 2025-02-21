from fastapi import APIRouter
from sqlalchemy import select

from src.database import SessionDep
from src.posts.models import Post
from src.posts.schemas import PostCreate

post_router = APIRouter()


@post_router.get("")
async def get_all_posts(session: SessionDep):
    stmt = select(Post)
    result = await session.execute(stmt)
    users = result.scalars().all()
    return users


@post_router.post("")
async def create_post(session: SessionDep, post_data: PostCreate):
    post = Post(**post_data.model_dump())
    session.add(post)
    await session.commit()
    return post