from fastapi.security import HTTPBearer
from fastapi_sqlalchemy import db

from models.carbrand import CarBrand
from schemas.carbrand import CarBrandSchema

class CarBrandService(object):
    __instance = None

    reusable_oauth2 = HTTPBearer(
        scheme_name='Authorization'
    )

    @staticmethod
    def get_all_carbrand():
        carbrands = db.session.query(CarBrand).all()
        return carbrands

    @staticmethod
    def get_carbrand(id: str):
        current_carbrand = db.session.query(CarBrand).filter(CarBrand.id == id).first()
        return current_carbrand

    @staticmethod
    def create_carbrand(data: CarBrandSchema):
        new_carbrand = CarBrand(
            id = data.id,
            name = data.name,
            logo = data.logo,
            describe = data.describe,
            number_of_models = data.number_of_models,
            status = data.status,
            created_by = data.created_by,
            created_at = data.created_at,
            updated_by = data.updated_by,
            updated_at = data.updated_at,
            deleted_by = data.deleted_by,
            deleted_at = data.deleted_at,
            deleted = data.deleted,
        )
        db.session.add(new_carbrand)
        db.session.commit()
        return new_carbrand