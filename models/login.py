from pydantic import BaseModel,Field,EmailStr
from typing import Optional

class login(BaseModel):
    id_login:Optional[int]=None
    email:EmailStr= Field(...,description='Email User')
    password:str=Field(...,min_length=5,max_length=256)
    nickname:str=Field(...,max_length=20)
    # = ... significa que no puede ser nulo
    