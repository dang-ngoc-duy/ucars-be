import datetime as _dt
import pydantic as _pydantic

class _BaseCarBrandSchema(_pydantic.BaseModel):
    name: str
    logo: str
    describe: str

    class Config:
        orm_mode = True

class CarBrandSchema(_BaseCarBrandSchema):
    id: str
    status: bool | None
    created_by: str | None
    created_at: _dt.datetime | None
    updated_by: str | None
    updated_at: _dt.datetime | None
    deleted_by: str | None
    deleted_at: _dt.datetime | None
    deleted: bool | None

class GetCarBrandSchema(_BaseCarBrandSchema):
    id: str | None
    name: str | None
    logo: str | None
    describe: str | None
    status: bool | None
    created_by: str | None
    created_at: _dt.datetime | None
    updated_by: str | None
    updated_at: _dt.datetime | None
    deleted_by: str | None
    deleted_at: _dt.datetime | None
    deleted: bool | None

    class Config:
        orm_mode = True