from pydantic import BaseModel



class AccountBase(BaseModel):
    name : str
    email : str
    password : str


class LoginBase(BaseModel):
    email : str
    password : str