FROM python:3.10


ENV PYTHONUNBUFFERED 1

RUN apt-get update -y
RUN apt-get -y install binutils libproj-dev gdal-bin  python3-lxml
RUN apt-get -y install libmemcached-dev

RUN mkdir /code
WORKDIR /code

ADD requirements.txt /code/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# copy entrypoint.sh

# Django service

ADD . /code/

# create unprivileged user
RUN adduser --disabled-password --gecos '' myuser