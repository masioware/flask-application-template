# official base image
FROM python:3.10-alpine

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /flask-application-template

# copy project files
COPY start.sh ./
COPY requirements.txt ./
COPY /app ./app

# install dependencies
RUN pip install -r requirements.txt
RUN pip install gunicorn

# run entrypoint
ENTRYPOINT ["./start.sh"]