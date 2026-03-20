#!/usr/bin/env bash
set -o errexit
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='ibrahim').exists() or User.objects.create_superuser('ibrahim', 'karanjaibrahim141@gmail.com', 'Admin@2026!')" | python manage.py shell
