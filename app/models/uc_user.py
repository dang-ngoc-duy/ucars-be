# UCUser Model
import sqlalchemy as _sql

import db.base as _db

class UCUser(_db.Base):
    __tablename__='uc_user'

    username = _sql.Column(_sql.String, primary_key=True, index=True, nullable=False)
    password = _sql.Column(_sql.String, index=True)