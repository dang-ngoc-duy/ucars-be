# Car Model
import datetime as _dt
from email.policy import default
import sqlalchemy as _sql

import db.base as _db

class Car(_db.Base):
    __tablename__='car'

    id = _sql.Column(_sql.String, primary_key=True, index=True, nullable=False)
    brand_id = _sql.Column(_sql.String, _sql.ForeignKey('carbrand.id'), index=True, nullable=False)
    name = _sql.Column(_sql.String)
    describe = _sql.Column(_sql.String)
    image = _sql.Column(_sql.String)
    registration_year = _sql.Column(_sql.Integer)
    transmission = _sql.Column(_sql.String)
    type = _sql.Column(_sql.String)
    door = _sql.Column(_sql.Integer)
    price = _sql.Column(_sql.Float)
    coe_category = _sql.Column(_sql.String)
    body_type = _sql.Column(_sql.String)
    body_size = _sql.Column(_sql.String)
    fuel_type = _sql.Column(_sql.String)
    fuel_consum = _sql.Column(_sql.String)
    engine_capacity = _sql.Column(_sql.String)
    range = _sql.Column(_sql.String)
    airbags = _sql.Column(_sql.Integer)
    lane_keep_assist = _sql.Column(_sql.Boolean, default=False)
    cruise_control = _sql.Column(_sql.Boolean, default=False)
    headlight = _sql.Column(_sql.Boolean, default=False)
    wheelbase = _sql.Column(_sql.Boolean, default=False)
    rim = _sql.Column(_sql.Boolean, default=False)
    seat = _sql.Column(_sql.Integer)
    smart_key = _sql.Column(_sql.Boolean, default=False)
    bluetooth = _sql.Column(_sql.Boolean, default=False)
    hub = _sql.Column(_sql.Boolean, default=False)
    status = _sql.Column(_sql.Boolean, default=False)
    created_by = _sql.Column(_sql.String, index=True)
    created_at = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
    updated_by = _sql.Column(_sql.String, index=True)
    updated_at = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
    deleted_by = _sql.Column(_sql.String, index=True)
    deleted_at = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
    deleted = _sql.Column(_sql.Boolean, default=False)