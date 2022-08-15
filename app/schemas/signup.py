import pydantic as _pydantic

class SignupSchema(_pydantic.BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True