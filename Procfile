release: python manage.py migrate --no-input --settings=config.settings.production
web: gunicorn config.wsgi
