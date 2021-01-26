FROM python:3.8.1-alpine

MAINTAINER David Ltd.

RUN apk add --update --no-cache \
    # Dependencies for Pillow
    build-base \
    libjpeg-turbo-dev \
    zlib-dev \
    libffi-dev \
    # Dependencies for Postgres
    postgresql-dev

RUN mkdir /app
WORKDIR /app

ADD . /app

# Handle dependencies
RUN pip install pipenv && \
    pipenv install

RUN pipenv run python3 manage.py makemigrations
RUN pipenv run python3 manage.py migrate
RUN pipenv run python3 manage.py collectstatic --noinput
RUN pipenv run uwsgi --ini /app/config/uwsgi/uwsgi.ini --http :8000