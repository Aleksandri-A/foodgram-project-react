#!/bin/sh

python manage.py migrate;
python manage.py collectstatic --noinput;
gunicorn -b 0:8070 backend.wsgi;
