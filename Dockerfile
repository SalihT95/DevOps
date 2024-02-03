# pull official base image
FROM python:3.11.3-slim-buster

#set work directory 
WORKDIR /usr/src/app

#set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#install dependencies
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

#copy project
COPY . /usr/src/app/

#expose the port the app will run on
EXPOSE 5000

#command to run on container start
CMD ["python", "rickandmorty.py"]