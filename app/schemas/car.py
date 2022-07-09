import datetime as _dt
import pydantic as _pydantic

class _BaseCarSchema(_pydantic.BaseModel):
    name: str = None
    describe: str = None
    image: str = None
    
    class Config:
        orm_mode = True

class CarSchema(_BaseCarSchema):
    id: str = None
    brand_id: str
    registration_year: int | None
    transmission: str | None
    type: str | None
    door: int | None
    price: float | None
    coe_category: str | None
    body_type: str | None
    body_size: str | None
    fuel_type: str | None
    fuel_consum: str | None
    engine_capacity: str | None
    range: str | None
    airbags: int | None
    lane_keep_assist: bool | None
    cruise_control: bool | None
    headlight: bool | None
    wheelbase: bool | None
    rim: bool | None
    seat: int | None
    smart_key: bool | None
    bluetooth: bool | None
    hub: bool | None
    status: bool | None
    created_by: str | None
    created_at: _dt.datetime | None
    updated_by: str | None
    updated_at: _dt.datetime | None
    deleted_by: str | None
    deleted_at: _dt.datetime | None
    deleted: bool | None

class GetCarSchema(_BaseCarSchema):
    pass
    class Config:
        orm_mode = True