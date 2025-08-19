from fastapi import APIRouter
from src.router.IPL import router as ipl_router

router = APIRouter(
    prefix="/ipl",
    tags=["IPL"]
)


router.include_router(ipl_router)
