from fastapi import APIRouter, HTTPException
from sqlalchemy import select
from starlette import status

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


@post_router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(session: SessionDep, post_id: int):
    stmt = select(Post).where(Post.id == post_id)
    result = await session.execute(stmt)
    post = result.scalar_one_or_none()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Post not found'
        )
    await session.delete(post)
    await session.commit()
    return {'message': 'Post deleted successfully'}


@post_router.put("/{post_id}")
async def update_post(session: SessionDep, post_id: int, post_data: PostCreate):
    stmt = select(Post).where(Post.id == post_id)
    result = await session.execute(stmt)
    post = result.scalar_one_or_none()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Post not found'
        )
    post.content = post_data.content
    await session.commit()
    return post