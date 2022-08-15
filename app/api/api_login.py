import logging
from fastapi import APIRouter, HTTPException
from fastapi_sqlalchemy import db
from core.security import verify_password, create_access_token, get_password_hash
from schemas.login import LoginSchema
from models.uc_user import UCUser

from helpers.exception_handler import CustomException

logger = logging.getLogger()
router = APIRouter()

# [POST] - /api/v1/login
@router.post("")
def login(request_data: LoginSchema) -> str:
    """
    API Login
    """
    # try:
    user = db.session.query(UCUser).filter(UCUser.username == request_data.username).first()

    if (user != None):
        temp_obj = user.__dict__
        print(temp_obj['password'])
        hashed_pwd = temp_obj['password']
        if verify_password(request_data.password, hashed_pwd) == False:
            raise HTTPException(status_code=404, detail="Incorrect username or password")
        else:
            token = create_access_token(request_data.username)
            return {
                'msg': 'Login Success!',
                'token': token
            }
    else:
        raise HTTPException(status_code=404, detail="User not found")
    # except Exception as e:
    #     raise CustomException(http_code=400, code='400', message=str(e))