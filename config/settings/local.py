# -*- coding: utf-8 -*-
"""
Django settings for local development environment.

- Run in Debug mode
- Add Django Debug Toolbar
"""

from .base import *  # noqa: F403

# DATABASE
# ----------------------------------------------------------------------------

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(ROOT_DIR, 'db.sqlite3'),
    }
}

# DEBUG
# ----------------------------------------------------------------------------
DEBUG = True  # noqa: F405
TEMPLATES[0]["OPTIONS"]["debug"] = DEBUG  # noqa: F405
SECRET_KEY = "localsecretkey"

# django-debug-toolbar
# ----------------------------------------------------------------------------
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware", ]  # noqa: F405
INSTALLED_APPS += ["debug_toolbar", ]  # noqa: F405
INTERNAL_IPS = ["127.0.0.1"]
DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": [
        "debug_toolbar.panels.redirects.RedirectsPanel",
    ],
    "SHOW_TEMPLATE_CONTEXT": True,
}
