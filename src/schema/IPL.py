from pydantic import BaseModel


class IplAddDetails(BaseModel):
    name : str
    gmail : str
    pasword : str
