#!/bin/bash
python manage.py collectstatic --no-input --settings=config.settings.production
python manage.py migrate --no-input --settings=config.settings.production
python manage.py loadpikau --settings=config.settings.production
