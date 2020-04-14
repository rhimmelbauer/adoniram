FROM python:3-alpine

# Make sure django is installed
RUN pip install django

# Create a project folder in the container
RUN mkdir webpage

#You make your project the working directory
WORKDIR webpage

#You copy any local file to the container.
COPY . .

# You create the project
#RUN django-admin startproject adoniram

# CMD sh

CMD python manage.py runserver 0.0.0.0:8000

