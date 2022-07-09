from fastapi import APIRouter

from api import api_carbrand
from api import api_car

router = APIRouter()

router.include_router(api_carbrand.router, tags=["carbrand"], prefix="/carbrands")
router.include_router(api_car.router, tags=["car"], prefix="/car")