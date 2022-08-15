import logging
from fastapi import APIRouter
from fastapi_sqlalchemy import db
from models.uc_user import UCUser
from schemas.signup import SignupSchema
from core.security import get_password_hash

from helpers.exception_handler import CustomException

logger = logging.getLogger()
router = APIRouter()

# [POST] - /api/v1/signup
@router.post("")
def signup(request_data: SignupSchema) -> str:
    """
    API Signup
    """
    try:
        isUserExist = db.session.query(UCUser).filter(UCUser.username == request_data.username).first()
        if isUserExist:
            return {
                'msg': 'User already exists!'
            }
        else:
            new_user = UCUser(
                username = request_data.username,
                password = get_password_hash(request_data.password)
            )
            db.session.add(new_user)
            db.session.commit()
            return {
                'msg': 'Regist Success!'
            }

    except Exception as e:
        raise CustomException(http_code=400, code='400', message=str(e))