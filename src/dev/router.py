from fastapi import APIRouter


dev_router = APIRouter()

@dev_router.get("")
def dev():
    return {"message": "Hello, World!"}