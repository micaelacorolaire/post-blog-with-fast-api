from pydantic import BaseModel,Field
from typing import Optional
from datetime import datetime
class publications(BaseModel):
    id_publication:Optional[int]=None
    title:str=Field(...,min_length=10,max_length=60)
    content:str=Field(...,min_length=500,max_length=1000)
    pub_date:datetime=Field(...,description="Publication Date",default_factory=datetime.now)
    author:str=Field(...,max_length=15)
    