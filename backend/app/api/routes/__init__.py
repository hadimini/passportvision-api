from fastapi import APIRouter

from app.api.routes.passport import router as passport_router


api_router = APIRouter()
api_router.include_router(passport_router, prefix="/passport", tags=["passport"])
