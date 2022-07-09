# CarBrand Model
import datetime as _dt
from email.policy import default
import sqlalchemy as _sql

import db.base as _db

class CarBrand(_db.Base):
    __tablename__='carbrand'

    id = _sql.Column(_sql.String, primary_key=True, index=True, nullable=False)
    name = _sql.Column(_sql.String, index=True)
    logo = _sql.Column(_sql.String, index=True)
    describe = _sql.Column(_sql.String, index=True)
    status = _sql.Column(_sql.Boolean, default=False)
    created_by = _sql.Column(_sql.String, index=True)
    created_at = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
    updated_by = _sql.Column(_sql.String, index=True)
    updated_at = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
    deleted_by = _sql.Column(_sql.String, index=True)
    deleted_at = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
    deleted = _sql.Column(_sql.Boolean, default=False)