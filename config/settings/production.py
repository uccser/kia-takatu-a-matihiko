# -*- coding: utf-8 -*-
"""
Django settings for production environment.

- Load secret values from environment variables.
"""

from .base import *  # noqa: F403
import django_heroku

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Activate Django-Heroku.
DEBUG = True
django_heroku.settings(locals())
