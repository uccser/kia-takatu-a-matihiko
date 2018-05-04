# -*- coding: utf-8 -*-
"""Django settings for kia-takatu-a-matihiko project."""

import os

BASE_DIR = os.path.abspath(os.path.join(__file__, "../../../"))

# APP CONFIGURATION
# ----------------------------------------------------------------------------
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "whitenoise.runserver_nostatic",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = []

# Apps specific for this project go here.
LOCAL_APPS = [
    "pikau.apps.PikauConfig",
]

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = THIRD_PARTY_APPS + DJANGO_APPS + LOCAL_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",

]

# Allow all host headers
ALLOWED_HOSTS = ['*']

# DEBUG
# ----------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = False

# GENERAL CONFIGURATION
# ----------------------------------------------------------------------------
TIME_ZONE = "NZ"
LANGUAGE_CODE = "en-NZ"
USE_I18N = True
USE_L10N = True
USE_TZ = True
TIME_FORMAT = "fA"

DATETIME_INPUT_FORMATS = [
    "%d/%m/%Y %H:%M:%S",
    "%d/%m/%Y %H:%M:%S.%f",
    "%d/%m/%Y %H:%M",
    "%d/%m/%Y",
    "%d/%m/%y %H:%M:%S",
    "%d/%m/%y %H:%M:%S.%f",
    "%d/%m/%y %H:%M",
    "%d/%m/%y",
    "%d-%m-%Y %H:%M:%S",
    "%d-%m-%Y %H:%M:%S.%f",
    "%d-%m-%Y %H:%M",
    "%d-%m-%Y",
]

DATE_INPUT_FORMATS = [
    "%d/%m/%Y",
    "%d/%m/%y",
    "%d-%m-%Y",
    "%d-%m-%y",
]

TIME_INPUT_FORMATS = [
    "%H:%M:%S",
    "%H:%M",
]

# TEMPLATE CONFIGURATION
# ----------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
        "DIRS": [
            str(os.path.join(BASE_DIR, "templates")),
        ],
        "OPTIONS": {
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
            "debug": DEBUG,
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
            # https://docs.djangoproject.com/en/dev/ref/templates/api/#loader-types
            "loaders": [
                "django.template.loaders.filesystem.Loader",
                "django.template.loaders.app_directories.Loader",
            ],
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ],
            "libraries": {
                "render_html_field": "config.templatetags.render_html_field",
                "get_item": "config.templatetags.get_item",
            },
        },
    },
]

# STATIC FILE CONFIGURATION
# ------------------------------------------------------------------------------
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_URL = "/staticfiles/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]
# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# URL Configuration
# ------------------------------------------------------------------------------
ROOT_URLCONF = "config.urls"

# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = "config.wsgi.application"

# PASSWORD VALIDATION
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
# ------------------------------------------------------------------------------

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# PASSWORD STORAGE SETTINGS
# ------------------------------------------------------------------------------
# See https://docs.djangoproject.com/en/dev/topics/auth/passwords/#using-argon2-with-django
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.BCryptPasswordHasher",
]


# OTHER SETTINGS
# ------------------------------------------------------------------------------
PIKAU_CONTENT_BASE_PATH = os.path.join(BASE_DIR, "pikau/content")
CUSTOM_VERTO_TEMPLATES = os.path.join(BASE_DIR, "utils/custom_converter_templates/")
