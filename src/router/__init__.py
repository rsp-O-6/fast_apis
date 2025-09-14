from fastapi import APIRouter
from src.router.IPL import router as ipl_router
from src.router.account import router as account_router

router = APIRouter()


router.include_router(ipl_router)
router.include_router(account_router)
