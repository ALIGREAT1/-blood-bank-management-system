#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input

python manage.py migrate

python manage.py shell -c "import os; from django.contrib.auth import get_user_model; User=get_user_model(); username=os.environ.get('DJANGO_SUPERUSER_USERNAME'); email=os.environ.get('DJANGO_SUPERUSER_EMAIL',''); password=os.environ.get('DJANGO_SUPERUSER_PASSWORD'); User.objects.create_superuser(username, email, password) if username and password and not User.objects.filter(username=username).exists() else print('Superuser already exists or credentials missing')"