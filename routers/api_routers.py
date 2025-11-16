from fastapi import APIRouter

router = APIRouter(prefix="/api")

@router.get("/")
async def home():
    data = {
        "id":"1",
        "name":"alok"
    }
    return data