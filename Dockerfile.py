#python version for docker image
FROM python:3.12-slim

##set the working dir in the conatiner
WORKDIR /code  # code becomes parent dir for exiting repo

# Copy the requirements file into the container at /app
COPY ./requirements.txt /code/requirements.txt

# Install the dependencies
RUN pip install  -r /code/requirements.txt

# Copy the code from app folder  into the container at /code
COPY ./app /code/app

# Copy the rest of the application code into the container

#set enviroment variable
ENV WANDB_API_KEY=""
ENV MODEL_PATH="" # model trained then need the version upadated    
#ENV PORT=8080
# Expose the port the app runs on
#Expose $PORT
EXPOSE 8080
#fastapi run app/main.py --port 8080 --host
#CMD['fastapi', 'run', 'app/main.py', '--port', '8080']
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
#CMD ["sh","-c","uvicorn.app.main:app --host 0.0.0.0 --port $PORT --reload"]



