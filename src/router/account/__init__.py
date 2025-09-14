from fastapi import APIRouter, Depends
from .registration import  router as registration_router
from .login import router as login_router

router = APIRouter(
    prefix="/account",
    tags=["account"])

router.include_router(registration_router)
router.include_router(login_router)