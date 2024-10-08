#!/bin/bash
set -ex

git fetch origin
git reset --hard origin/main

pdm sync

source .venv/bin/activate
export DJANGO_SETTINGS_MODULE=pycon.settings.production
python manage.py migrate --noinput
sudo systemctl restart pycon.service
