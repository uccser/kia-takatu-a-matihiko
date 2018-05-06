# -*- coding: utf-8 -*-
"""
Django settings for production environment.

- Load secret values from environment variables.
"""

from .base import *  # noqa: F403
import django_heroku

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Activate Django-Heroku.
django_heroku.settings(locals())
STATIC_URL = "/staticfiles/"

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#default-from-email
DEFAULT_FROM_EMAIL = env(  # noqa: F405
    "DJANGO_DEFAULT_FROM_EMAIL",
    default="Kia Takatū ā-Matihiko: Content Pipeline Assistant <noreply@ktam-content-assistant.herokuapp.com>"
)
# https://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = env("DJANGO_SERVER_EMAIL", default=DEFAULT_FROM_EMAIL)  # noqa: F405
# https://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = env("DJANGO_EMAIL_SUBJECT_PREFIX", default="[Kia Takatū ā-Matihiko: Content Pipeline Assistant] ")  # noqa: F405

# Anymail (Mailgun)
# ------------------------------------------------------------------------------
# https://anymail.readthedocs.io/en/stable/installation/#installing-anymail
INSTALLED_APPS += ["anymail"]  # noqa F405
EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"
# https://anymail.readthedocs.io/en/stable/installation/#anymail-settings-reference
ANYMAIL = {
    "MAILGUN_API_KEY": env("MAILGUN_API_KEY"),  # noqa: F405
    "MAILGUN_SENDER_DOMAIN": env("MAILGUN_DOMAIN")  # noqa: F405
}
