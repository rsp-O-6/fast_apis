from fastapi import APIRouter

from .ipl import router as ipl_router


router = APIRouter()
router.include_router(ipl_router)



