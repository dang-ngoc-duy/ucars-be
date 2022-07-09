from core.config import settings

import sqlalchemy as _sql
import sqlalchemy.orm as _orm
import sqlalchemy.ext.declarative as _declarative

engine = _sql.create_engine(settings.DATABASE_URL, pool_pre_ping=True)

SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = _declarative.declarative_base()