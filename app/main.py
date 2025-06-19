import torch
import io  

from pydantic import BaseModel # it is datatype ,it is installed FASTAPI

# this a 'data model' for output of  the actual fruit classifier model
class Result(BaseModel):
    category:str
    confidence:float

