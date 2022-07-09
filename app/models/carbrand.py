from sqlalchemy import Boolean, Column, Integer, String, DateTime

from app.models.base import BareBaseModel

class CarBrand(BareBaseModel):
    br_id = Column(String, primary_key=True, nullable=False)
    name = Column(String)
    numof_model = Column(Integer)
    logo = Column(String)
    describe = Column(String)
    status = Column(Boolean)
    created_by = Column(String)
    updated_by = Column(String)
    deleted_by = Column(String)
    deleted_at = Column(DateTime)
    deleted = Column(Boolean, default=False)