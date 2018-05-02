# -*- coding: utf-8 -*-
"""Django settings for kia-takatu-a-matihiko project."""

import os

ROOT_DIR = os.path.abspath(os.path.join(__file__, "../../../"))

# APP CONFIGURATION
# ----------------------------------------------------------------------------
DJANGO_APPS = [
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
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# DEBUG
# ----------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = False

# GENERAL CONFIGURATION
# ----------------------------------------------------------------------------
TIME_ZONE = "NZ"
LANGUAGE_CODE = "en-NZ"
SITE_ID = 1
USE_I18N = False
USE_L10N = False
USE_TZ = False
TIME_FORMAT = "fA"

# TEMPLATE CONFIGURATION
# ----------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
        "DIRS": [
            str(os.path.join(ROOT_DIR, "templates")),
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
                "django.template.context_processors.static",
            ],
            "libraries": {
                "render_html_field": "config.templatetags.render_html_field",
            },
        },
    },
]

# STATIC FILE CONFIGURATION
# ------------------------------------------------------------------------------
STATIC_ROOT = os.path.join(ROOT_DIR, "staticfiles")
STATIC_URL = "/staticfiles/"
STATICFILES_DIRS = [
    os.path.join(ROOT_DIR, "static"),
]
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# URL Configuration
# ------------------------------------------------------------------------------
ROOT_URLCONF = "config.urls"

# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = "config.wsgi.application"

PIKAU_CONTENT_BASE_PATH = os.path.join(ROOT_DIR, "pikau/content")
CUSTOM_VERTO_TEMPLATES = os.path.join(ROOT_DIR, "utils/custom_converter_templates/")
