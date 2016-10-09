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

1. New app, name, connect to github.

2. On Resources > Add-ons, provision a new "Heroku Postgress".

3. Set the following enviorment variables:


`ENVIRONMENT` set to PRODUCTION (other options are DEVELOPMENT or STAGING)

`DJANGO_SECRET_KEY` generate a new and secret one

`DATABASE_URL` for the postgress instance, heroku automatically fills it.

4. Add Buildpack: `heroku/python`

# Notes

* If DATABASE_URL is empty, Django will use a sqlite3.db, its the default for local development.