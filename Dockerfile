# syntax=docker/dockerfile:1
FROM python:3.9-alpine
ENV PYTHONUNBUFFERED=1

# direcory creation process
RUN mkdir /code
WORKDIR /code
COPY . /code/

#install dependenciees
COPY requirements.txt /code/
RUN pip install -r requirements.txt
