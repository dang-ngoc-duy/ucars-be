import pydantic as _pydantic

class LoginSchema(_pydantic.BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True