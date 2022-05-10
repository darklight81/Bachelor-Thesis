#!/bin/bash
apt-get update && apt-get install -y netcat


echo "Entrypoint reached"

    echo "Waiting for postgres..."

    while ! nc -z db 5432; do
        sleep 0.1
    done

    echo "PostgreSQL started"

python manage.py myauth zero
python manage.py makemigrations myauth
python manage.py makemigrations
python manage.py showmigrations
python manage.py migrate myauth
python manage.py migrate 
