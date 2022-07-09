import db.base as _db

def add_tables():
    return _db.Base.metadata.create_all(bind=_db.engine)

def get_db():
    db = _db.SessionLocal()
    try:
        yield db
    finally:
        db.close()
