from pydantic import BaseModel,Field,EmailStr
from typing import Optional

class personaldatauser(BaseModel):
    id_personaldatauser :Optional[int]=None 
    name:str=Field(...,min_length=2,max_length=20)
    lastname:str=Field(...,max_length=20)
    age:int=Field(...,gt=18,lt=100)
    nacionality:str=Field(...,max_length=30)
    email:EmailStr= Field(...,description='Email User')
    password:str=Field(...,min_length=5,max_length=256)
    