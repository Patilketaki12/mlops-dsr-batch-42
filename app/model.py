# define function load_model

import os
import wandb
from loadotenv import load_env # removed in GCP deployment

import torch
from torchvision.models import resnet18, ResNet



#todo: remember to delete the use of the 
# loadotenv and os.getenv entries 
# when we use the Docker image later
MODELS_DIR='models'
os.makedirs(MODELS_DIR, exist_ok=True)
load_env() # This will be removed for the GCP deployment
wandb_api_key =  os.environ.get("WANDB_API_KEY")
model_path=os.environ.get("FULL_PATH_TO_MODEL")
if wandb_api_key:    
    wandb.login(key=wandb_api_key)
    #print({wandb_api_key})

#TODO:remeber to delete this print statement

print(model_path)

def download_artifact():   
    artifact = wandb.Api().artifact(model_path, type='model')
    artifact.download(root=MODELS_DIR)


download_artifact()













