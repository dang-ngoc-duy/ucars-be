from fastapi import APIRouter

from api import api_carbrand
from api import api_car
from api import api_login
from api import api_signup

router = APIRouter()

router.include_router(api_carbrand.router, tags=["carbrand"], prefix="/carbrands")
router.include_router(api_car.router, tags=["car"], prefix="/car")
router.include_router(api_login.router, tags=["login"], prefix="/login")
router.include_router(api_signup.router, tags=["signup"], prefix="/signup")