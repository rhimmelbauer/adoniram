FROM python:3-alpine

# Update alpine and install mysql client
RUN apk update && \
    apk add --no-cache build-base mysql-dev mysql-client

# Make sure django is installed
RUN pip install django mysqlclient

# Create a project folder in the container
RUN mkdir webpage

#You make your project the working directory
WORKDIR webpage

COPY requirements.txt .
RUN pip install -r requirements.txt

#You copy any local file to the container.
COPY . .

# You create the project
#RUN django-admin startproject adoniram

# CMD sh

CMD python manage.py runserver 0.0.0.0:8000

