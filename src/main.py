from fastapi import FastAPI

from src.dev.router import dev_router
from src.posts.router import post_router

app = FastAPI()
app.include_router(post_router, prefix="/posts", tags=["posts"])
app.include_router(dev_router, prefix="/dev", tags=["dev"])

