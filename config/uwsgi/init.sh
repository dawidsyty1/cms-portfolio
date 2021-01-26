#!/bin/bash
pipenv run python3 manage.py makemigrations
pipenv run python3 manage.py migrate
pipenv run python3 manage.py collectstatic --noinput
pipenv run uwsgi --ini /app/config/uwsgi/uwsgi.ini --http :8000
