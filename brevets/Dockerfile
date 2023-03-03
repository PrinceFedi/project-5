FROM python:3.8
LABEL maintainer="fedia@uoregon.edu"
RUN apt-get update -y
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

