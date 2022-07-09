from fastapi.security import HTTPBearer
from fastapi_sqlalchemy import db

from models.car import Car
from schemas.car import CarSchema

class CarService(object):
    __instance = None

    reusable_oauth2 = HTTPBearer(
        scheme_name='Authorization'
    )

    @staticmethod
    def get_all_car():
        cars = db.session.query(Car).all()
        return cars
        
    @staticmethod
    def get_car(id: str):
        current_car = db.session.query(Car).filter(Car.id == id).first()
        return current_car

    @staticmethod
    def create_car(data: CarSchema):
        new_car = Car(
            id = data.id,
            name = data.name,
            describe = data.describe,
            image = data.image,
            brand_id = data.brand_id,
            registration_year = data.registration_year,
            transmission = data.transmission,
            type = data.type,
            door = data.door,
            price = data.price,
            coe_category = data.coe_category,
            body_type = data.body_type,
            body_size = data.body_size,
            fuel_type = data.fuel_type,
            fuel_consum = data.fuel_consum,
            engine_capacity = data.engine_capacity,
            range = data.range,
            airbags = data.airbags,
            lane_keep_assist = data.lane_keep_assist,
            cruise_control = data.cruise_control,
            headlight = data.headlight,
            wheelbase = data.wheelbase,
            rim = data.rim,
            seat = data.seat,
            smart_key = data.smart_key,
            bluetooth = data.bluetooth,
            hub = data.hub,
            status = data.status,
            created_by = data.created_by,
            created_at = data.created_at,
            updated_by = data.updated_by,
            updated_at = data.updated_at,
            deleted_by = data.deleted_by,
            deleted_at = data.deleted_at,
            deleted = data.deleted,
        )
        db.session.add(new_car)
        db.session.commit()
        return new_car