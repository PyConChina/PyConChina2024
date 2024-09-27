#!/bin/bash
set -ex

python manage.py migrate --noinput
gunicorn pycon.wsgi:application
