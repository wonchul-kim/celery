#!/bin/sh

### wait till /app/backend directory is ready
until cd /app/backend
do
    echo "Waiting for server volume..."
done

### wait till database is ready and run migration
until python manage.py migrate
do
    echo "Waiting for db to be ready..."
    sleep 2
done

### collect static files
python manage.py collectstatic --noinput

# python manage.py createsuperuser --noinput

### start gunicorn server for development
gunicorn backend.wsgi --bind 0.0.0.0:8000 --workers 4 --threads 4

# for debug
#python manage.py runserver 0.0.0.0:8000
