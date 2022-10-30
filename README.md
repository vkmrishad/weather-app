# weather-app
Simple weather web app using Python/Django

![example workflow](https://github.com/vkmrishad/weather_app/actions/workflows/black.yaml/badge.svg?branch=main)
![example workflow](https://github.com/vkmrishad/weather_app/actions/workflows/django-ci.yaml/badge.svg?branch=main)
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

## Clone

    git clone https://github.com/vkmrishad/weather_app.git
    or
    git git@github.com:vkmrishad/weather_app.git

## System dependencies

* [Python: 3.9+](https://www.python.org/downloads/)
* [sqlite](https://www.sqlite.org/index.html)
* [pre-commit](https://pre-commit.com/) - optional

## Environment and Package Management
Install [Poetry](https://python-poetry.org/)

    $ pip install poetry
    or
    $ pip3 install poetry

Activate or Create Env

    $ poetry shell

Install Packages from Poetry

    $ poetry install

NB: When using virtualenv, install from [requirements.txt](/requirements.txt) using `$ pip install -r requirements.txt`.
For environment variables follow [sample.env](/sample.env)

## Migrate DB

    $ python manage.py migrate
    or
    $ ./manage.py migrate

## Collect static

    $ python manage.py collectstatic
    or
    $ ./manage.py collectstatic

## Runserver

    $ python manage.py runserver 0.0.0.0:8000
    or
    $ ./manage.py runserver 0.0.0.0:8000

# Run async

    $ gunicorn -w 3 -k uvicorn.workers.UvicornWorker weather_app.asgi:application --bind=0.0.0.0:8000

## Test

    $ python manage.py test apps
    or
    $ ./manage.py test apps

## Create superuser
Create superuser to test admin feature

    $ python manage.py createsuperuser
    or
    $ ./manage.py createsuperuser


#### Access server: http://127.0.0.1:8000
#### Access Admin: http://127.0.0.1:8000/admin/
