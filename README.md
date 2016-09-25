# Django Heroku Boilerplate

Django 1.10+ initial setup ready to deploy on Heroku.

Features dev enviorments (development, staging and production), database url, Procfile, app.json and multi app folder structure.

## Setup

* Your local virtual enviorment:

`mkvirtualenv --python=/usr/local/bin/python3 APPNAME`

`workon APPNAME`

`pip install -r requirements/development.txt`

* Run:

`python manage.py runserver`

## Customize

* Rename APPNAME to your app name (find and replace in files and folders everywhere).

* Use apps/APPNAME/appmodel.py as a template for your models to make the multi app folder structure work.

## Deploy on Heroku

* On Heroku set the following enviorment variables:

`DATABASE_URL` (postgress)

`ENVIRONMENT` (DEVELOPMENT, STAGING or PRODUCTION)

`DJANGO_SECRET_KEY` (generate a new and secret one)

# Notes

* If DATABASE_URL is empty, Django will use a sqlite3.db