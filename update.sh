#!/bin/bash
set -ex

cd "$(dirname "$0")"

git fetch origin
git reset --hard origin/main

~/.local/bin/pdm sync

source .venv/bin/activate
export DJANGO_SETTINGS_MODULE=pycon.settings.production
python manage.py migrate --noinput
python manage.py collectstatic --noinput
sudo systemctl restart pycon.service
