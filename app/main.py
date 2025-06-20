import torch
import io  


from pydantic import BaseModel # it is datatype ,it is installed FASTAPI
from fastapi import FastAPI,File,UploadFile,Depends
from torchvision.models import Resent

# this a 'data model' for output of  the actual fruit classifier model
class Result(BaseModel):
    category:str
    confidence:float

app=FastAPI()

@app.get("/")
def read_root():
    return {'meassage':'Welcome to fruit Classifier API- use/predict to classsify images'}

@app.post("/predict",response_model=Result)
async def predict(
    input_image:UploadFile=File(...),
    model:Resent=Depends(load_model),
    ...
)