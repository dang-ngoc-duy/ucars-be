import logging
from fastapi import APIRouter, HTTPException
from fastapi_sqlalchemy import db

from helpers.exception_handler import CustomException

from schemas.base import DataResponse

from schemas.car import CarSchema, GetCarSchema
from services.car import CarService
from models.car import Car

logger = logging.getLogger()
router = APIRouter()

# [GET] - /api/v1/car
@router.get("", response_model=DataResponse[list[GetCarSchema]])
def get_all_car() -> list[Car]:
    """
    API Get Cars
    """
    try:
        cars = CarService().get_all_car()
        return DataResponse().success_response(data=cars)
    except Exception as e:
        raise HTTPException(status_code=400, detail=logger.error(e))

# [GET] - /api/v1/car/{id}
@router.get("/{id}", response_model=DataResponse[CarSchema])
def get_car(id: str) -> Car:
    """
    API Get Car By ID
    """
    try:
        current_car = CarService().get_car(id)
        return DataResponse().success_response(data=current_car)
    except Exception as e:
        raise HTTPException(status_code=400, detail=logger.error(e))

# [POST] - /api/v1/car
@router.post("", response_model=DataResponse[CarSchema])
def create_car(car_data: CarSchema) -> Car:
    """
    API Create Car
    """
    try:
        car = db.session.query(Car).filter(Car.id == car_data.id).first()
        if car:
            raise Exception('Car already exists')
        new_car = CarService().create_car(car_data)
        return DataResponse().success_response(data=new_car)
    except Exception as e:
        raise CustomException(http_code=400, code='400', message=str(e))