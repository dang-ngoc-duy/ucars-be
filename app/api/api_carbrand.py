import logging
from typing import List
from fastapi import APIRouter, HTTPException
from fastapi_sqlalchemy import db

from helpers.exception_handler import CustomException

from schemas.base import DataResponse
from schemas.carbrand import CarBrandSchema, GetCarBrandSchema
from services.carbrand import CarBrandService
from models.carbrand import CarBrand

logger = logging.getLogger()
router = APIRouter()

# [GET] - /api/v1/carbrands
@router.get("", response_model=DataResponse[list[GetCarBrandSchema]])
def get_all_carbrand() -> list[CarBrand]:
    """
    API Get CarBrands
    """
    try:
        carbrands = CarBrandService().get_all_carbrand()
        return DataResponse().success_response(data=carbrands)
    except Exception as e:
        raise HTTPException(status_code=400, detail=logger.error(e))

# [GET] - /api/v1/carbrands/{id}
@router.get("/{id}", response_model=DataResponse[CarBrandSchema])
def get_carbrand(id: str) -> CarBrand:
    """
    API Get CarBrands By ID
    """
    try:
        current_carbrand = CarBrandService().get_carbrand(id)
        return DataResponse().success_response(data=current_carbrand)
    except Exception as e:
        raise HTTPException(status_code=400, detail=logger.error(e))

# [POST] - /api/v1/carbrands
@router.post("", response_model=DataResponse[CarBrandSchema])
def create_carbrand(carbrand_data: CarBrandSchema) -> CarBrand:
    """
    API Create CarBrand
    """
    try:
        carbrand = db.session.query(CarBrand).filter(CarBrand.id == carbrand_data.id).first()
        if carbrand:
            raise Exception('Car brand already exists')
        new_carbrand = CarBrandService().create_carbrand(carbrand_data)
        return DataResponse().success_response(data=new_carbrand)
    except Exception as e:
        raise CustomException(http_code=400, code='400', message=str(e))