from sqlalchemy import Boolean, Column, Float, ForeignKey, DateTime, String
from sqlalchemy.orm import relationship

from app.models.base import BareBaseModel
from app.models.carbrand import CarBrand


class Car(BareBaseModel):
    carbrand = relationship(CarBrand)

    car_id = Column(String, primary_key=True, nullable=False)
    br_id = Column(String, ForeignKey('carbrand.id'), nullable=False)
    name = Column(String)
    price = Column(Float)
    year = Column(String)
    created_by = Column(String)
    updated_by = Column(String)
    deleted_by = Column(String)
    deleted_at = Column(DateTime)
    deleted = Column(Boolean, default=False)